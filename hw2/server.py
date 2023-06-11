import asyncio
from grpc import aio
from threading import Lock
from collections import defaultdict

import sys
import random
import game_pb2 as game_proto
import game_pb2_grpc as game_proto_grpc
import time

class Room:
    def __init__(self):
        self.role_mapping = {}
        self.chats = []
        self.roles = ['mafia', 'civilian', 'civilian', 'sheriff']
        self.game_started = False

        self.starting_game_cv = asyncio.Condition()
        self.mutex = Lock()

        self.accused = defaultdict(int)
        self.day_cv = asyncio.Condition()
        self.person_accused = ""

        self.night_cv = asyncio.Condition()
        self.waiting = 0
        self.status_mapping = {}

        self.wait_speak = 0
        self.announce_cv = asyncio.Condition()
        self.can_tell= False
        self.mafias = []

        self.game_is_played = True

class Server(game_proto_grpc.ServerServicer):
    def __init__(self):
        self.rooms = {}
        self.room_ids = set()
        self.room_mutex = Lock()
        self.not_filled_rooms = defaultdict(int)
        for room_id in range(5000, 10000):
            self.room_ids.add(room_id)
            self.rooms[room_id] = Room()
        self.max_players = 4

    async def InitName(self, request, context):
        room = self.rooms[request.room_id]
        room.role_mapping[request.name] = ''
        room.status_mapping[request.name] = 'alive'
        room.chats.append(game_proto.Reply(message='%s joined the game' % request.name))
        return game_proto.Reply(message='Hello, %s!' % request.name)


    async def GetStream(self, request, context):
        i = 0
        room = self.rooms[request.room_id]
        while True and room.game_is_played:
            if i < len(room.chats):
                i += 1
                yield room.chats[i - 1]
            else:
                await asyncio.sleep(1)

    async def StartTheGameRequest(self, request, context):
        room = self.rooms[request.room_id]
        if len(room.role_mapping) != self.max_players:
            async with room.starting_game_cv:
                await room.starting_game_cv.wait()
        else:
            async with room.starting_game_cv:
                room.starting_game_cv.notify_all()

        if not room.game_started:
            room.chats.append(game_proto.Reply(message='game started'))
            room.game_started = True

        return game_proto.EmptyResponse()

    async def RoleAssignment(self, request, context):
        room = self.rooms[request.room_id]
        room.mutex.acquire()
        room.role_mapping[request.name] = room.roles.pop()
        room.mutex.release()
        return game_proto.Role(role=room.role_mapping[request.name])
    
    async def VotePattern(self, request):
        room = self.rooms[request.room_id]
        accused_person = request.name
        if accused_person in room.accused:
            room.accused[accused_person] += 1
        else:
            room.accused[accused_person] = 1


    async def VoteWithChat(self, request, context):
        await self.VotePattern(request)
        self.rooms[request.room_id].chats.append(game_proto.Reply(message=f'{request.username} has voted for {request.name}.'))
        return game_proto.EmptyResponse()
    
    async def VoteWithoutChat(self, request, context):
        await self.VotePattern(request)
        return game_proto.EmptyResponse()

    async def UsersInfo(self, request, context):
        room = self.rooms[request.room_id]
        users = ""
        statuses = ""
        for name, status in room.status_mapping.items():
            if name != request.name:
                users += name + ','
                statuses += status + ','
        return game_proto.UsersInfoMessage(names=users[:-1], statuses=statuses[:-1])

    async def CleanAccusedRequest(self, request, context):
        room = self.rooms[request.room_id]
        room.person_accused = ""
        return game_proto.EmptyResponse()

    async def GetRoomId(self, request, context):
        self.room_mutex.acquire()
        if len(self.not_filled_rooms) != 0:
            room_id = random.choice(list(self.not_filled_rooms.keys()))
            self.not_filled_rooms[room_id] += 1
            if self.not_filled_rooms[room_id] == self.max_players:
                self.not_filled_rooms.pop(room_id, None)
        else:
            room_id = random.choice(list(self.room_ids))
            self.room_ids.remove(room_id)
            self.not_filled_rooms[room_id] = 1
        self.room_mutex.release()
        return game_proto.RoomResponse(room_id=room_id)

    async def CheckGameEnding(self, request, context):
        room = self.rooms[request.room_id]
        count_mafia = 0
        count_citizens = 0
        for _, role in room.role_mapping.items():
            if role != 'mafia' and role != 'ghost':
                count_citizens += 1
            else:
                count_mafia += 1
        message = ''
        if count_mafia == 0:
            message = 'Citizens won'
            room.game_is_played = False
        elif count_mafia == count_citizens:
            message = 'Mafia won'
            room.game_is_played = False

        right = room.game_is_played
        if not right:
            self.room_mutex.acquire()
            self.room_ids.add(request.room_id)
            self.room_mutex.release()
        return game_proto.BoolReply(message=message, right=right)

    async def CheckAnnouncements(self, request, room):
        room.can_tell |= request.ready
        room.can_tell &= (len(room.mafias) != 0)
        room.wait_speak += 1

    async def AnnounceMafia(self, request, context):
        room = self.rooms[request.room_id]
        await self.CheckAnnouncements(request, room)

        if room.wait_speak != self.max_players:
            async with room.announce_cv:
                await room.announce_cv.wait()
                time.sleep(0.2)
        else:
            async with room.announce_cv:
                room.announce_cv.notify_all()
        if room.can_tell:
            room.chats.append(game_proto.Reply(message=f'The officer found out that {room.mafias.pop()} is mafia'))
        room.can_tell = False
        room.wait_speak = 0
        return game_proto.EmptyResponse()
    
    async def CheckPerson(self, request, context):
        room = self.rooms[request.room_id]
        person_to_check = request.name
        if room.role_mapping[person_to_check] == 'mafia':
            room.mafias.append(person_to_check)
            return game_proto.BoolReply(message=f'yes, {person_to_check} is mafia', right=True)
        else:
            return game_proto.BoolReply(message=f'{person_to_check} is not mafia', right=len(room.mafias))

    async def kill(self, room):
        people_with_max_votes = []
        max_votes = max(room.accused.values())
        for username, votes in room.accused.items():
            if votes == max_votes:
                people_with_max_votes.append(username)

        room.person_accused = random.choice(people_with_max_votes)
        room.status_mapping[room.person_accused] = "ghost"
        room.role_mapping.pop(room.person_accused, None)
    
    async def sum_up(self, room):
        room.accused = {}
        room.waiting = 0

    
    async def NightResult(self, request, context):
        room = self.rooms[request.room_id]
        room.waiting += 1
        if room.waiting != self.max_players:
            async with room.night_cv:
                await room.night_cv.wait()
                time.sleep(0.5)
        else:
            async with room.night_cv:
                room.night_cv.notify_all()

        if room.person_accused:
            return game_proto.Reply(message=room.person_accused)

        await self.kill(room)
        room.chats.append(game_proto.Reply(message=f'{room.person_accused} is dead'))
        await self.sum_up(room)
        return game_proto.Reply(message=room.person_accused)

    async def DayResult(self, request, context):
        room = self.rooms[request.room_id]
        room.waiting += 1
        if room.waiting != self.max_players:
            async with room.day_cv:
                await room.day_cv.wait()
                time.sleep(0.5)
        else:
            async with room.day_cv:
                room.day_cv.notify_all()

        if room.person_accused:
            return game_proto.Reply(message=room.person_accused)

        await self.kill(room)
        room.chats.append(game_proto.Reply(message=f'{room.person_accused} is dead'))
        await self.sum_up(room)
        if room.person_accused in room.mafias:
            room.mafias.remove(room.person_accused)
        return game_proto.Reply(message=room.person_accused)



async def serve():
    port = '22828'
    server = aio.server()
    game_proto_grpc.add_ServerServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:' + port)
    print(f'server is listening on port: {port}')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())