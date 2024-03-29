# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import contextlib
import re

from telethon import Button
from telethon.errors import MessageNotModifiedError
from telethon.events import CallbackQuery

from userbot import arankub

from ..Config import Config
from ..core.logger import logging

LOGS = logging.getLogger(__name__)


@arankub.tgbot.on(CallbackQuery(data=re.compile(r"^age_verifiarankion_true")))
async def age_verifiarankion_true(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "Given That It's A Stupid-Ass Decision, I've Elected To Ignore It.",
            alert=True,
        )
    await event.answer("Yes I'm 18+", alert=False)
    buttons = [
        Button.inline(
            text="Unsure / Change of Decision ❔",
            data="chg_of_decision_",
        )
    ]
    with contextlib.suppress(MessageNotModifiedError):
        await event.edit(
            text="To access this plugin type `.setdv ALLOW_NSFW True`",
            file="https://graph.org/file/85f3071c31279bcc280ef.jpg",
            buttons=buttons,
        )


@arankub.tgbot.on(CallbackQuery(data=re.compile(r"^age_verifiarankion_false")))
async def age_verifiarankion_false(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "Given That It's A Stupid-Ass Decision, I've Elected To Ignore It.",
            alert=True,
        )
    await event.answer("No I'm Not", alert=False)
    buttons = [
        Button.inline(
            text="Unsure / Change of Decision ❔",
            data="chg_of_decision_",
        )
    ]
    with contextlib.suppress(MessageNotModifiedError):
        await event.edit(
            text="GO AWAY KID !",
            file="https://graph.org/file/1140f16a883d35224e6a1.jpg",
            buttons=buttons,
        )


@arankub.tgbot.on(CallbackQuery(data=re.compile(r"^chg_of_decision_")))
async def chg_of_decision_(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "Given That It's A Stupid-Ass Decision, I've Elected To Ignore It.",
            alert=True,
        )
    await event.answer("Unsure", alert=False)
    buttons = [
        (
            Button.inline(text="Yes I'm 18+", data="age_verifiarankion_true"),
            Button.inline(text="No I'm Not", data="age_verifiarankion_false"),
        )
    ]
    with contextlib.suppress(MessageNotModifiedError):
        await event.edit(
            text="**ARE YOU OLD ENOUGH FOR THIS ?**",
            file="https://graph.org/file/238f2c55930640e0e8c56.jpg",
            buttons=buttons,
        )
