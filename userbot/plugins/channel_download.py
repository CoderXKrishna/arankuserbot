# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Special credits:
# [Radha](https://t.me/itsz_krish_babess) (For Channel Media Downloader Plugin)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


import contextlib
import os
import subprocess

from ..Config import Config
from ..helpers.tools import media_type
from . import arankub, edit_or_reply

plugin_category = "tools"


@arankub.arank_cmd(
    pattern="getc(?:\s|$)([\s\S]*)",
    command=("getc", plugin_category),
    info={
        "header": "To download channel media files",
        "description": "pass username and no of latest messages to check to command \
             so the bot will download media files from that latest no of messages to server ",
        "usage": "{tr}getc count channel_username",
        "examples": "{tr}getc 10 @arankuserbot17",
    },
)
async def get_media(event):
    arankty = event.pattern_match.group(1)
    limit = int(arankty.split(" ")[0])
    channel_username = str(arankty.split(" ")[1])
    tempdir = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, channel_username)
    with contextlib.suppress(BaseException):
        os.makedirs(tempdir)
    event = await edit_or_reply(event, "`Downloading Media From this Channel.`")
    msgs = await event.client.get_messages(channel_username, limit=limit)
    i = 0
    for msg in msgs:
        mediatype = await media_type(msg)
        if mediatype is not None:
            await event.client.download_media(msg, tempdir)
            i += 1
            await event.edit(
                f"Downloading Media From this Channel.\n **DOWNLOADED : **`{i}`"
            )
    ps = subprocess.Popen(("ls", tempdir), stdout=subprocess.PIPE)
    output = subprocess.check_output(("wc", "-l"), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'", " ")
    output = output.replace("\\n'", " ")
    await event.edit(
        f"Successfully downloaded {output} number of media files from {channel_username} to tempdir"
    )


@arankub.arank_cmd(
    pattern="geta(?:\s|$)([\s\S]*)",
    command=("geta", plugin_category),
    info={
        "header": "To download channel all media files",
        "description": "pass username to command so the bot will download all media files from that latest no of messages to server ",
        "note": "there is limit of 3000 messages for this process to prevent API limits. that is will download all media files from latest 3000 messages",
        "usage": "{tr}geta channel_username",
        "examples": "{tr}geta @arankuserbot17",
    },
)
async def get_media(event):
    channel_username = event.pattern_match.group(1)
    tempdir = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, channel_username)
    with contextlib.suppress(BaseException):
        os.makedirs(tempdir)
    event = await edit_or_reply(event, "`Downloading All Media From this Channel.`")
    msgs = await event.client.get_messages(channel_username, limit=3000)
    i = 0
    for msg in msgs:
        mediatype = await media_type(msg)
        if mediatype is not None:
            await event.client.download_media(msg, tempdir)
            i += 1
            await event.edit(
                f"Downloading Media From this Channel.\n **DOWNLOADED : **`{i}`"
            )
    ps = subprocess.Popen(("ls", tempdir), stdout=subprocess.PIPE)
    output = subprocess.check_output(("wc", "-l"), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'", "")
    output = output.replace("\\n'", "")
    await event.edit(
        f"Successfully downloaded {output} number of media files from {channel_username} to tempdir"
    )
