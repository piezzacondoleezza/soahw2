# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import game_pb2 as game__pb2


class ServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitName = channel.unary_unary(
                '/Server/InitName',
                request_serializer=game__pb2.NameRequest.SerializeToString,
                response_deserializer=game__pb2.Reply.FromString,
                )
        self.GetRoomId = channel.unary_unary(
                '/Server/GetRoomId',
                request_serializer=game__pb2.EmptyRequest.SerializeToString,
                response_deserializer=game__pb2.RoomResponse.FromString,
                )
        self.GetStream = channel.unary_stream(
                '/Server/GetStream',
                request_serializer=game__pb2.RoomRequest.SerializeToString,
                response_deserializer=game__pb2.Reply.FromString,
                )
        self.StartTheGameRequest = channel.unary_unary(
                '/Server/StartTheGameRequest',
                request_serializer=game__pb2.RoomRequest.SerializeToString,
                response_deserializer=game__pb2.EmptyResponse.FromString,
                )
        self.RoleAssignment = channel.unary_unary(
                '/Server/RoleAssignment',
                request_serializer=game__pb2.NameRequest.SerializeToString,
                response_deserializer=game__pb2.Role.FromString,
                )
        self.UsersInfo = channel.unary_unary(
                '/Server/UsersInfo',
                request_serializer=game__pb2.NameRequest.SerializeToString,
                response_deserializer=game__pb2.UsersInfoMessage.FromString,
                )
        self.VoteWithChat = channel.unary_unary(
                '/Server/VoteWithChat',
                request_serializer=game__pb2.AccuseRequest.SerializeToString,
                response_deserializer=game__pb2.EmptyResponse.FromString,
                )
        self.VoteWithoutChat = channel.unary_unary(
                '/Server/VoteWithoutChat',
                request_serializer=game__pb2.AccuseRequest.SerializeToString,
                response_deserializer=game__pb2.EmptyResponse.FromString,
                )
        self.CheckPerson = channel.unary_unary(
                '/Server/CheckPerson',
                request_serializer=game__pb2.NameRequest.SerializeToString,
                response_deserializer=game__pb2.BoolReply.FromString,
                )
        self.DayResult = channel.unary_unary(
                '/Server/DayResult',
                request_serializer=game__pb2.RoomRequest.SerializeToString,
                response_deserializer=game__pb2.Reply.FromString,
                )
        self.NightResult = channel.unary_unary(
                '/Server/NightResult',
                request_serializer=game__pb2.RoomRequest.SerializeToString,
                response_deserializer=game__pb2.Reply.FromString,
                )
        self.AnnounceMafia = channel.unary_unary(
                '/Server/AnnounceMafia',
                request_serializer=game__pb2.AnnounceMafiaRequest.SerializeToString,
                response_deserializer=game__pb2.EmptyRequest.FromString,
                )
        self.CleanAccusedRequest = channel.unary_unary(
                '/Server/CleanAccusedRequest',
                request_serializer=game__pb2.RoomRequest.SerializeToString,
                response_deserializer=game__pb2.EmptyResponse.FromString,
                )
        self.CheckGameEnding = channel.unary_unary(
                '/Server/CheckGameEnding',
                request_serializer=game__pb2.RoomRequest.SerializeToString,
                response_deserializer=game__pb2.BoolReply.FromString,
                )


class ServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InitName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoomId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartTheGameRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RoleAssignment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UsersInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteWithChat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteWithoutChat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckPerson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DayResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NightResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AnnounceMafia(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CleanAccusedRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckGameEnding(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitName': grpc.unary_unary_rpc_method_handler(
                    servicer.InitName,
                    request_deserializer=game__pb2.NameRequest.FromString,
                    response_serializer=game__pb2.Reply.SerializeToString,
            ),
            'GetRoomId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoomId,
                    request_deserializer=game__pb2.EmptyRequest.FromString,
                    response_serializer=game__pb2.RoomResponse.SerializeToString,
            ),
            'GetStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetStream,
                    request_deserializer=game__pb2.RoomRequest.FromString,
                    response_serializer=game__pb2.Reply.SerializeToString,
            ),
            'StartTheGameRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.StartTheGameRequest,
                    request_deserializer=game__pb2.RoomRequest.FromString,
                    response_serializer=game__pb2.EmptyResponse.SerializeToString,
            ),
            'RoleAssignment': grpc.unary_unary_rpc_method_handler(
                    servicer.RoleAssignment,
                    request_deserializer=game__pb2.NameRequest.FromString,
                    response_serializer=game__pb2.Role.SerializeToString,
            ),
            'UsersInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.UsersInfo,
                    request_deserializer=game__pb2.NameRequest.FromString,
                    response_serializer=game__pb2.UsersInfoMessage.SerializeToString,
            ),
            'VoteWithChat': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteWithChat,
                    request_deserializer=game__pb2.AccuseRequest.FromString,
                    response_serializer=game__pb2.EmptyResponse.SerializeToString,
            ),
            'VoteWithoutChat': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteWithoutChat,
                    request_deserializer=game__pb2.AccuseRequest.FromString,
                    response_serializer=game__pb2.EmptyResponse.SerializeToString,
            ),
            'CheckPerson': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckPerson,
                    request_deserializer=game__pb2.NameRequest.FromString,
                    response_serializer=game__pb2.BoolReply.SerializeToString,
            ),
            'DayResult': grpc.unary_unary_rpc_method_handler(
                    servicer.DayResult,
                    request_deserializer=game__pb2.RoomRequest.FromString,
                    response_serializer=game__pb2.Reply.SerializeToString,
            ),
            'NightResult': grpc.unary_unary_rpc_method_handler(
                    servicer.NightResult,
                    request_deserializer=game__pb2.RoomRequest.FromString,
                    response_serializer=game__pb2.Reply.SerializeToString,
            ),
            'AnnounceMafia': grpc.unary_unary_rpc_method_handler(
                    servicer.AnnounceMafia,
                    request_deserializer=game__pb2.AnnounceMafiaRequest.FromString,
                    response_serializer=game__pb2.EmptyRequest.SerializeToString,
            ),
            'CleanAccusedRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.CleanAccusedRequest,
                    request_deserializer=game__pb2.RoomRequest.FromString,
                    response_serializer=game__pb2.EmptyResponse.SerializeToString,
            ),
            'CheckGameEnding': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckGameEnding,
                    request_deserializer=game__pb2.RoomRequest.FromString,
                    response_serializer=game__pb2.BoolReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Server', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Server(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InitName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/InitName',
            game__pb2.NameRequest.SerializeToString,
            game__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRoomId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/GetRoomId',
            game__pb2.EmptyRequest.SerializeToString,
            game__pb2.RoomResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Server/GetStream',
            game__pb2.RoomRequest.SerializeToString,
            game__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartTheGameRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/StartTheGameRequest',
            game__pb2.RoomRequest.SerializeToString,
            game__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RoleAssignment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/RoleAssignment',
            game__pb2.NameRequest.SerializeToString,
            game__pb2.Role.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UsersInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/UsersInfo',
            game__pb2.NameRequest.SerializeToString,
            game__pb2.UsersInfoMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteWithChat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/VoteWithChat',
            game__pb2.AccuseRequest.SerializeToString,
            game__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteWithoutChat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/VoteWithoutChat',
            game__pb2.AccuseRequest.SerializeToString,
            game__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckPerson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/CheckPerson',
            game__pb2.NameRequest.SerializeToString,
            game__pb2.BoolReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DayResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/DayResult',
            game__pb2.RoomRequest.SerializeToString,
            game__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NightResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/NightResult',
            game__pb2.RoomRequest.SerializeToString,
            game__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AnnounceMafia(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/AnnounceMafia',
            game__pb2.AnnounceMafiaRequest.SerializeToString,
            game__pb2.EmptyRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CleanAccusedRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/CleanAccusedRequest',
            game__pb2.RoomRequest.SerializeToString,
            game__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckGameEnding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/CheckGameEnding',
            game__pb2.RoomRequest.SerializeToString,
            game__pb2.BoolReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
