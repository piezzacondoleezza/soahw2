from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AccuseRequest(_message.Message):
    __slots__ = ["name", "room_id", "username"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    room_id: int
    username: str
    def __init__(self, username: _Optional[str] = ..., name: _Optional[str] = ..., room_id: _Optional[int] = ...) -> None: ...

class AnnounceMafiaRequest(_message.Message):
    __slots__ = ["ready", "room_id"]
    READY_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ready: bool
    room_id: int
    def __init__(self, ready: bool = ..., room_id: _Optional[int] = ...) -> None: ...

class BoolReply(_message.Message):
    __slots__ = ["message", "right"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    message: str
    right: bool
    def __init__(self, message: _Optional[str] = ..., right: bool = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EmptyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NameRequest(_message.Message):
    __slots__ = ["name", "room_id"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    room_id: int
    def __init__(self, name: _Optional[str] = ..., room_id: _Optional[int] = ...) -> None: ...

class Reply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ["role"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: str
    def __init__(self, role: _Optional[str] = ...) -> None: ...

class RoomRequest(_message.Message):
    __slots__ = ["room_id"]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: int
    def __init__(self, room_id: _Optional[int] = ...) -> None: ...

class RoomResponse(_message.Message):
    __slots__ = ["room_id"]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: int
    def __init__(self, room_id: _Optional[int] = ...) -> None: ...

class UsersInfoMessage(_message.Message):
    __slots__ = ["names", "statuses"]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    names: str
    statuses: str
    def __init__(self, names: _Optional[str] = ..., statuses: _Optional[str] = ...) -> None: ...
