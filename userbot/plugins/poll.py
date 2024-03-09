# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import random

from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll

from userbot import arankub

from ..core.managers import edit_or_reply
from . import Build_Poll, reply_id

plugin_category = "extra"


@arankub.arank_cmd(
    pattern="poll(?:\s|$)([\s\S]*)",
    command=("poll", plugin_category),
    info={
        "header": "To create a poll.",
        "description": "If you doesnt give any input it sends a default poll",
        "usage": ["{tr}poll", "{tr}poll question ; option 1; option2"],
        "examples": "{tr}poll Are you an early bird or a night owl ;Early bird ; Night owl",
    },
)
async def pollcreator(arankpoll):
    "To create a poll"
    reply_to_id = await reply_id(arankpoll)
    if string := "".join(arankpoll.text.split(maxsplit=1)[1:]):
        arankinput = string.split(";")
        if len(arankinput) > 2 and len(arankinput) < 12:
            options = Build_Poll(arankinput[1:])
            try:
                await arankpoll.client.send_message(
                    arankpoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=arankinput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await arankpoll.delete()
            except PollOptionInvalidError:
                await edit_or_reply(
                    arankpoll,
                    "`A poll option used invalid data (the data may be too long).`",
                )
            except ForbiddenError:
                await edit_or_reply(arankpoll, "`This chat has forbidden the polls`")
            except Exception as e:
                await edit_or_reply(arankpoll, str(e))
        else:
            await edit_or_reply(
                arankpoll,
                "Make sure that you used Correct syntax `.poll question ; option1 ; option2`",
            )

    else:
        options = Build_Poll(["Yah sure 😊✌️", "Nah 😏😕", "Whatever die sur 🥱🙄"])
        try:
            await arankpoll.client.send_message(
                arankpoll.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="👆👆So do you guys agree with this?",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await arankpoll.delete()
        except PollOptionInvalidError:
            await edit_or_reply(
                arankpoll, "`A poll option used invalid data (the data may be too long).`"
            )
        except ForbiddenError:
            await edit_or_reply(arankpoll, "`This chat has forbidden the polls`")
        except Exception as e:
            await edit_or_reply(arankpoll, str(e))
