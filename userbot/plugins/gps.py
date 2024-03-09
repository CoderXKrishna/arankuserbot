# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from geopy.geocoders import Nominatim
from telethon.tl import types

from userbot import arankub

from ..core.managers import edit_or_reply
from ..helpers import reply_id

plugin_category = "extra"


@arankub.arank_cmd(
    pattern="gps ([\s\S]*)",
    command=("gps", plugin_category),
    info={
        "header": "To send the map of the given loarankion.",
        "usage": "{tr}gps <place>",
        "examples": "{tr}gps Hyderabad",
    },
)
async def gps(event):
    "Map of the given loarankion."
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    arankevent = await edit_or_reply(event, "`finding.....`")
    geoloarankor = Nominatim(user_agent="arankuserbot")
    if geoloc := geoloarankor.geocode(input_str):
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.client.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            caption=f"**Loarankion : **`{input_str}`",
            reply_to=reply_to_id,
        )
        await arankevent.delete()
    else:
        await arankevent.edit("`i coudn't find it`")
