# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from userbot import arankub

from ..core.managers import edit_or_reply
from ..helpers.utils import _format

plugin_category = "tools"


# yaml_format is ported from uniborg
@arankub.arank_cmd(
    pattern="json$",
    command=("json", plugin_category),
    info={
        "header": "To get details of that message in json format.",
        "usage": "{tr}json reply to message",
    },
)
async def _(event):
    "To get details of that message in json format."
    arankevent = await event.get_reply_message() if event.reply_to_msg_id else event
    the_real_message = arankevent.stringify()
    await edit_or_reply(event, the_real_message, parse_mode=_format.parse_pre)


@arankub.arank_cmd(
    pattern="yaml$",
    command=("yaml", plugin_category),
    info={
        "header": "To get details of that message in yaml format.",
        "usage": "{tr}yaml reply to message",
    },
)
async def _(event):
    "To get details of that message in yaml format."
    arankevent = await event.get_reply_message() if event.reply_to_msg_id else event
    the_real_message = _format.yaml_format(arankevent)
    await edit_or_reply(event, the_real_message, parse_mode=_format.parse_pre)
