# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import os

from PIL import Image

from userbot.core.logger import logging
from userbot.core.managers import edit_or_reply
from userbot.helpers.functions.vidtools import take_screen_shot
from userbot.helpers.tools import fileinfo, media_type, meme_type
from userbot.helpers.utils.utils import runcmd

LOGS = logging.getLogger(__name__)


class arankConverter:
    async def _media_check(self, reply, dirct, file, memetype):
        if not os.path.isdir(dirct):
            os.mkdir(dirct)
        arankfile = os.path.join(dirct, file)
        if os.path.exists(arankfile):
            os.remove(arankfile)
        try:
            arankmedia = reply if os.path.exists(reply) else None
        except TypeError:
            if memetype in ["Video", "Gif"]:
                dirct = "./temp/arankfile.mp4"
            elif memetype == "Audio":
                dirct = "./temp/arankfile.mp3"
            arankmedia = await reply.download_media(dirct)
        return arankfile, arankmedia

    async def to_image(
        self, event, reply, dirct="./temp", file="meme.png", noedits=False, rgb=False
    ):
        memetype = await meme_type(reply)
        mediatype = await media_type(reply)
        if memetype == "Document":
            return event, None
        arankevent = (
            event
            if noedits
            else await edit_or_reply(
                event, "`Transfiguration Time! Converting to ....`"
            )
        )
        arankfile, arankmedia = await self._media_check(reply, dirct, file, memetype)
        if memetype == "Photo":
            im = Image.open(arankmedia)
            im.save(arankfile)
        elif memetype in ["Audio", "Voice"]:
            await runcmd(f"ffmpeg -i '{arankmedia}' -an -c:v copy '{arankfile}' -y")
        elif memetype in ["Round Video", "Video", "Gif"]:
            await take_screen_shot(arankmedia, "00.00", arankfile)
        if mediatype == "Sticker":
            if memetype == "Animated Sticker":
                arankcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{arankmedia}' '{arankfile}'"
                stdout, stderr = (await runcmd(arankcmd))[:2]
                if stderr:
                    LOGS.info(stdout + stderr)
            elif memetype == "Video Sticker":
                await take_screen_shot(arankmedia, "00.00", arankfile)
            elif memetype == "Static Sticker":
                im = Image.open(arankmedia)
                im.save(arankfile)
        if arankmedia and os.path.exists(arankmedia):
            os.remove(arankmedia)
        if os.path.exists(arankfile):
            if rgb:
                img = Image.open(arankfile)
                if img.mode != "RGB":
                    img = img.convert("RGB")
                img.save(arankfile)
            return arankevent, arankfile, mediatype
        return arankevent, None

    async def to_sticker(
        self, event, reply, dirct="./temp", file="meme.webp", noedits=False, rgb=False
    ):
        filename = os.path.join(dirct, file)
        response = await self.to_image(event, reply, noedits=noedits, rgb=rgb)
        if response[1]:
            image = Image.open(response[1])
            image.save(filename, "webp")
            os.remove(response[1])
            return response[0], filename, response[2]
        return response[0], None

    async def to_webm(
        self, event, reply, dirct="./temp", file="animate.webm", noedits=False
    ):
        # //Hope u dunt kang :/ @Jisan7509
        memetype = await meme_type(reply)
        if memetype not in [
            "Round Video",
            "Video Sticker",
            "Gif",
            "Video",
        ]:
            return event, None
        arankevent = (
            event
            if noedits
            else await edit_or_reply(event, "__🎞Converting into Animated sticker..__")
        )
        arankfile, arankmedia = await self._media_check(reply, dirct, file, memetype)
        media = await fileinfo(arankmedia)
        h = media["height"]
        w = media["width"]
        w, h = (-1, 512) if h > w else (512, -1)
        await runcmd(
            f"ffmpeg -to 00:00:02.900 -i '{arankmedia}' -vf scale={w}:{h} -c:v libvpx-vp9 -crf 30 -b:v 560k -maxrate 560k -bufsize 256k -an '{arankfile}'"
        )  # pain
        if os.path.exists(arankmedia):
            os.remove(arankmedia)
        return (arankevent, arankfile) if os.path.exists(arankfile) else (arankevent, None)

    async def to_gif(
        self, event, reply, dirct="./temp", file="meme.mp4", maxsize="5M", noedits=False
    ):
        memetype = await meme_type(reply)
        mediatype = await media_type(reply)
        if memetype not in [
            "Round Video",
            "Video Sticker",
            "Animated Sticker",
            "Video",
            "Gif",
        ]:
            return event, None
        arankevent = (
            event
            if noedits
            else await edit_or_reply(
                event, "`Transfiguration Time! Converting to ....`"
            )
        )
        arankfile, arankmedia = await self._media_check(reply, dirct, file, memetype)
        if mediatype == "Sticker":
            if memetype == "Video Sticker":
                await runcmd(f"ffmpeg -i '{arankmedia}' -c copy '{arankfile}'")
            elif memetype == "Animated Sticker":
                await runcmd(f"lottie_convert.py '{arankmedia}' '{arankfile}'")
        if arankmedia.endswith(".gif"):
            await runcmd(f"ffmpeg -f gif -i '{arankmedia}' -fs {maxsize} -an '{arankfile}'")
        else:
            await runcmd(
                f"ffmpeg -i '{arankmedia}' -c:v libx264 -fs {maxsize} -an '{arankfile}'"
            )
        if arankmedia and os.path.exists(arankmedia):
            os.remove(arankmedia)
        return (arankevent, arankfile) if os.path.exists(arankfile) else (arankevent, None)


Convert = arankConverter()
