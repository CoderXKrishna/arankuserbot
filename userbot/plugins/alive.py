# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import random
import re
import time
from datetime import datetime
from platform import python_version

import requests
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from userbot import StartTime, arankub, arankversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import arankalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"


@arankub.arank_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    ANIME = None
    arank_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    if "ANIME" in arank_caption:
        data = requests.get("https://animechan.vercel.app/api/random").json()
        ANIME = f"**“{data['quote']}” - {data['character']} ({data['anime']})**"
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    arankevent = await edit_or_reply(event, "`so here you go kanishka represents...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  😘 "
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**Mere mr.hitlerrr puchte gusse mein mujhse kya h vo mere?? **"
    ARANK_IMG = Config.ALIVE_PIC
    caption = arank_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        ANIME=ANIME,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        arankver=arankversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if ARANK_IMG:
        arank = list(arank_IMG.split())
        PIC = random.choice(arank)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await arankevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                arankevent,
                f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{PIC}`",
            )
    else:
        await edit_or_reply(
            arankevent,
            caption,
        )


temp = """{ALIVE_TEXT}
**{EMOJI} unhe ache se pta hai :** `{He is the world of my mine which starts on him and end only on him but still unko jaan na rehta toh bta dete aaj kya hai vo humare liye dekho to be honest ek gaane ki mast si do lines yaad aarhi unke liye pehle toh vo gaaleta hunn fir aage batate kya hai advocate sahab humare liye😌❤️}`
**{EMOJI} Tareef karunn kya unki jinhone tumhe banaya :** `{yeah i m very thankyou to my bestuuu kanha ji unhone meko ye anmol ratna meko diya hai🦋❤️}`
**{EMOJI} or dusra mummy papa ji unka toh jitna thankyou krunn utna kam :** `{aaj ke time mein itni achi up bringing mere heere ko itna nikhar diya hai unhone ki 1000 logo ke beech mein alag najar aaye hn thodu sa gussa hojate hai but ache dil ke log jo muh pe bolna pasand krte sach bolte ye fact h vo thoddu sa gussa krne wale hote mere bade bachuuu bhi unmein se he ek...jaan basti hai jaan meri uss ek praani mein or vo puchta hunn kon mai meko i love you beyond infinity mr.hitlerrr🥺❤️🤧}`
**{EMOJI} meri baat na hopati jab jo frustation :** `{bhi pe nikalti gussa banke vo abhi he janta bs or idhar ye budha bolta yaad aaye tab toh msg krre na shi mein lagta meko yaad na aati🥺🤧}`
**{EMOJI} Budhe i wanna do kabaddi with youuuu :** `{Budhe mere pe hazaar reason ho chuke hai 8 reason or milte he 1008 pe teri gardan kat dunga mai jaise krishna bhagwàan ji ne kaati thi so sudhar jaa aise drame na krrak kr samjha praan nikal jaate idhar or udhar nautanki tang krne se baaj na aawe apne paap ka ghada bhar mat budhe nhi toh acha nhi hoga tere liye samjha budhe}`
**{EMOJI} Your Robot Rabby:** {mention}"""


def arankalive_text():
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  😘 "
    arank_caption = "**arankuserbot is Up and Running**\n"
    arank_caption += f"**{EMOJI} unhe ache se pta hai :** `{{He is the world of my mine which starts on him and end only on him}}\n`"
    arank_caption += f"**{EMOJI} Tareef karunn kya unki jinhone tumhe banaya :** `Budhe i wanna do kabaddi with youuuu`\n"
    arank_caption += f"**{EMOJI} or dusra mummy papa ji unka toh jitna thankyou krunn utna kam :** `meri baat na hopati jab jo frustation()`\n"
    arank_caption += f"**{EMOJI} Your Robot Rabby:** {mention}\n"
    return arank_caption


@arankub.arank_cmd(
    pattern="ialive$",
    command=("ialive", plugin_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}ialive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, "ialive")
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@arankub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await arankalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
