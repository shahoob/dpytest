
from typing import List, Union, Dict, Callable, Coroutine, Any, Optional, NoReturn, BinaryIO, Tuple
import pathlib
import asyncio
import discord
import discord.state as state
import discord.http as dhttp

JsonVals = Union[str, int, bool, Dict[str, 'JsonVals'], List['JsonVals']]
JsonDict = Dict[str, JsonVals]
Callback = Callable[[Any, ...], Coroutine]
AnyChannel = Union[discord.abc.GuildChannel, discord.abc.PrivateChannel]


class BackendConfig:
    callbacks: Dict[str, Callable[[...], Coroutine]]
    state: "FakeState"

_cur_config: BackendConfig

class FakeHttp(dhttp.HTTPClient):

    fileno: int = ...
    state: FakeState

    def __init__(self, loop: asyncio.AbstractEventLoop = ...) -> None: ...

    def _get_higher_locs(self, num: int) -> Dict[str, Any]: ...

    async def request(self, *args, **kwargs) -> NoReturn: ...

    async def send_files(self, channel_id: int, *, files: Tuple[BinaryIO, ...], content: str = ..., tts: bool = ..., embed: JsonDict = ..., nonce: int = ...) -> JsonDict: ...

    async def send_message(self, channel_id: int, content: str, *, tts: bool = ..., embed: JsonDict = ..., nonce: int = ...) -> JsonDict: ...

    async def application_info(self) -> JsonDict: ...

    async def change_my_nickname(self, guild_id: int, nickname: str, *, reason: str = ...) -> JsonDict: ...

class FakeState(state.ConnectionState):

    http: FakeHttp

    def __init__(self, client: discord.Client, http: dhttp.HTTPClient, user: discord.ClientUser = ..., loop: asyncio.AbstractEventLoop = ...) -> None: ...

def get_state() -> FakeState: ...

def set_callback(cb: Callback, event: str) -> None: ...

def get_callback(event: str) -> Optional[Callback]: ...

def remove_callback(event: str) -> Optional[Callback]: ...

def _dispatch_event(event: str, *args: Any, **kwargs: Any) -> None: ...

def make_guild(name: str, members: List[discord.Member] = ..., channels: List[AnyChannel] = ..., roles: List[JsonDict] = ...,
               owner: bool = ..., id_num: int = ...) -> discord.Guild: ...

def make_role(name: str, guild: discord.Guild, id_num: int = ..., colou: int = ..., permissions: int = ..., hoist: bool = ..., mentionable: bool = ...) -> discord.Role: ...

def make_text_channel(name: str, guild: discord.Guild, position: int = ..., id_num: int = ...) -> discord.TextChannel: ...

def make_user(username: str, discrim: Union[str, int], avatar: str = ..., id_num: int = ...) -> discord.User: ...

def make_member(user: discord.User, guild: discord.Guild, nick: str = ..., roles: List[discord.Role] = ...) -> discord.Member: ...

def make_message(content: str, author: Union[discord.User, discord.Member], channel: AnyChannel, id_num: int = ...) -> discord.Message: ...

def make_attachment(filename: pathlib.Path, name: str = ...) -> discord.Attachment: ...

def configure(client: discord.Client) -> None: ...

def main() -> None: ...