from __future__ import print_function

import grpc
import game_pb2
import game_pb2_grpc
import asyncio
import time
import sys
from simple_term_menu import TerminalMenu
import random
import string

def gen_random_str():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(10))

class Client:
    def __init__(self, bot=False):
        self.user_name = ''
        self.room_id = 0
        self.stub = game_pb2_grpc.ServerStub(grpc.aio.insecure_channel('localhost:22828'))
        self.role = ''
        self.bot=bot

    def get_room_id(self):
        return self.room_id

    async def set_room_id(self):
        response = await self.stub.GetRoomId(game_pb2.EmptyRequest())
        self.room_id = response.room_id

    async def init_user(self, user_name, room_id):
        self.user_name = user_name
        self.room_id = room_id
        await self.stub.InitName(game_pb2.NameRequest(name=self.user_name, room_id=self.room_id))

    async def start_process(self):
        tasks = [self.game_play(), self.notifications_from_server()]
        await asyncio.gather(*tasks)

    async def notifications_from_server(self):
        stub = self.stub
        async for note in stub.GetStream(game_pb2.RoomResponse(room_id=self.room_id)):
            print(note.message, flush=True)
    
    async def sheriff_day_announce(self):
        tell = False
        if self.role == 'sheriff':
            print("would you name the mafia?", flush=True)
            if self.bot:
                tell=True
            else:
                options = ["Yes", "No"]
                terminal_menu = TerminalMenu(options)
                menu_chosen_option = terminal_menu.show()
                if options[menu_chosen_option] == "Yes":
                    tell = True
        await self.stub.AnnounceMafia(game_pb2.AnnounceMafiaRequest(ready=tell, room_id=self.room_id))
        time.sleep(0.5)
    
    async def get_alive_list(self):
        response = await self.stub.UsersInfo(game_pb2.NameRequest(name=self.user_name, room_id=self.room_id))
        users = response.names.split(',')
        statuses = response.statuses.split(',')
        alive = []
        for i in range(len(users)):
            if statuses[i] == 'alive':
                alive.append(users[i])
        return alive
    
    async def choose_day_victim(self, alive_users):
        print('alive users: ', alive_users, flush=True)

        options = ["Skip", "Vote for someone"]
        terminal_menu = TerminalMenu(options)
        menu_chosen_option = terminal_menu.show()

        if options[menu_chosen_option] == "Vote for someone":
            terminal_menu = TerminalMenu(alive_users)
            menu_chosen_option = terminal_menu.show()
            await self.stub.VoteWithChat(game_pb2.AccuseRequest(username=self.user_name, name=alive_users[menu_chosen_option], room_id=self.room_id))

    async def choose_night_victim(self, alive_users):
        print('alive users: ', alive_users, flush=True)

        options = ["Skip", "Vote for someone"]
        terminal_menu = TerminalMenu(options)
        menu_chosen_option = terminal_menu.show()

        if options[menu_chosen_option] == "Vote for someone":
            terminal_menu = TerminalMenu(alive_users)
            menu_chosen_option = terminal_menu.show()
            await self.stub.VoteWithoutChat(game_pb2.AccuseRequest(username=self.user_name, name=alive_users[menu_chosen_option], room_id=self.room_id))


    async def sheriff_check(self, alive_users):
        options = ["Skip", "Vote for someone"]
        terminal_menu = TerminalMenu(options)
        menu_chosen_option = terminal_menu.show()

        if options[menu_chosen_option] == "Vote for someone":
            terminal_menu = TerminalMenu(alive_users)
            menu_chosen_option = terminal_menu.show()
            response = await self.stub.CheckPerson(game_pb2.NameRequest(username=self.user_name, name=alive_users[menu_chosen_option], room_id=self.room_id))
            print(response.message, flush=True)


    async def game_play(self):
        await self.stub.StartTheGameRequest(game_pb2.RoomRequest(room_id=self.room_id))
        time.sleep(2)
        response = await self.stub.RoleAssignment(game_pb2.NameRequest(name=self.user_name, room_id=self.room_id))
        time.sleep(2)
        print("Your role is here: ", response.role, flush=True)
        self.role = response.role

        day_round = 1
        night_round = 1

        while True:
            if day_round != 1:
                print(f'Day: {day_round}', flush=True)
                await self.sheriff_day_announce()
                alive = await self.get_alive_list()
                if self.role != 'ghost':

                    if self.bot:
                        await self.stub.VoteWithChat(game_pb2.AccuseRequest(username=self.user_name, name=random.choice(alive), room_id=self.room_id))
                    else:
                        await self.choose_day_victim(alive)
                response = await self.stub.DayResult(game_pb2.RoomRequest(room_id=self.room_id))
                if response.message == self.user_name:
                    self.role = "ghost"

            day_round += 1
            await self.stub.CleanAccusedRequest(game_pb2.RoomRequest(room_id=self.room_id))
            time.sleep(0.2)

            response = await self.stub.CheckGameEnding(game_pb2.RoomRequest(room_id=self.room_id))
            if not response.right:
                print(response.message, flush=True)
                break


            print(f'Night {night_round}', flush=True)
            alive = await self.get_alive_list()

            if self.role == 'mafia':
                if self.bot:
                    await self.stub.VoteWithoutChat(game_pb2.AccuseRequest(username=self.user_name, name=random.choice(alive), room_id=self.room_id))
                else:
                    await self.choose_night_victim(alive)

            elif self.role == 'sheriff':

                if self.bot:
                    response = await self.stub.CheckPerson(game_pb2.NameRequest(name=random.choice(alive), room_id=self.room_id))
                    print(response.message, flush=True)
                else:
                    await self.sheriff_check(alive)

            response = await self.stub.NightResult(game_pb2.RoomRequest(room_id=self.room_id))
            if response.message == self.user_name:
                self.role = "ghost"

            await self.stub.CleanAccusedRequest(game_pb2.RoomRequest(room_id=self.room_id))
            time.sleep(0.5)
            night_round += 1

            response = await self.stub.CheckGameEnding(game_pb2.RoomRequest(room_id=self.room_id))
            if not response.right:
                print(response.message, flush=True)
                break

        response = await self.stub.CheckGameEnding(game_pb2.RoomRequest(room_id=self.room_id))

async def run(bot=False):
    client = Client(bot)

    await client.set_room_id()
    room_id = client.get_room_id()
    print("Your room id is: ", room_id, flush=True)

    while True:
        if not bot:
            print('Print your name here: ', flush=True)
            name = input()
        else:
            name = gen_random_str()
            print(f'assigned to bot {name}', flush=True)

        response = await client.stub.UsersInfo(game_pb2.NameRequest(name="", room_id=client.room_id))
        users = response.names.split(',')
        if name in users:
            print("not original name", flush=True)
        else:
            break
    await client.init_user(name, room_id)
    await client.start_process()

if __name__ == "__main__":
    bot = False
    if len(sys.argv) >= 2:
        bot = True
    asyncio.run(run(bot))