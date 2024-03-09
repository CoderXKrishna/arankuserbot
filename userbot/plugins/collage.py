# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import os

from userbot import Convert, arankub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers import _arankutils, meme_type, reply_id

plugin_category = "utils"


@arankub.arank_cmd(
    pattern="collage(?:\s|$)([\s\S]*)",
    command=("collage", plugin_category),
    info={
        "header": "To create collage from still images extracted from video/gif.",
        "description": "Shows you the grid image of images extracted from video/gif. you can customize the Grid size by giving integer between 1 to 9 to cmd by default it is 3",
        "usage": "{tr}collage <1-9>",
    },
)
async def collage(event):
    "To create collage from still images extracted from video/gif."
    arankinput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    arankid = await reply_id(event)
    if not (reply and (reply.media)):
        return await edit_delete(event, "`Reply to a media file..`")
    mediacheck = await meme_type(reply)
    if mediacheck not in [
        "Round Video",
        "Gif",
        "Video Sticker",
        "Animated Sticker",
        "Video",
    ]:
        return await edit_delete(
            event, "`The replied message media type is not supported.`"
        )
    if arankinput:
        if not arankinput.isdigit():
            return await edit_delete(event, "`You input is invalid, check help`")

        arankinput = int(arankinput)
        if not 0 < arankinput < 10:
            await edit_or_reply(
                event,
                "__Why big grid you cant see images, use size of grid between 1 to 9\nAnyways changing value to max 9__",
            )
            arankinput = 9
    else:
        arankinput = 3
    await edit_or_reply(event, "```Collaging this may take several minutes..... 😁```")
    if mediacheck in ["Round Video", "Gif", "Video Sticker", "Video"]:
        if not os.path.isdir("./temp/"):
            os.mkdir("./temp/")
        aranksticker = await reply.download_media(file="./temp/")
        collagefile = aranksticker
    else:
        collage_file = await Convert.to_gif(
            event, reply, file="collage.mp4", noedits=True
        )
        collagefile = collage_file[1]
    if not collagefile:
        await edit_or_reply(
            event, "**Error:-** __Unable to process the replied media__"
        )
    endfile = "./temp/collage.png"
    arankcmd = f"vcsi -g {arankinput}x{arankinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await _arankutils.runcmd(arankcmd))[:2]
    if not os.path.exists(endfile) and os.path.exists(collagefile):
        os.remove(collagefile)
        return await edit_delete(
            event, "`Media is not supported, or try with smaller grid size`"
        )
    await event.client.send_file(
        event.chat_id,
        endfile,
        reply_to=arankid,
    )
    await event.delete()
    for files in (collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)
