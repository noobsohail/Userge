# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

from datetime import datetime

from pyrogram.raw.functions import Ping

from userge import userge, Message


@userge.on_cmd("ping", about={
    'header': "check how long it takes to ping your userbot"}, group=-1)
async def pingme(message: Message):
    start = datetime.now()
    await message.client.send(Ping(ping_id=0))
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**Pong!**\n`{m_s} ms`")