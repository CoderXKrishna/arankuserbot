# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import logging

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    handlers=[logging.FileHandler("arankub.log"), logging.StreamHandler()],
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

logging.getLogger("telethon.client.updates").setLevel(logging.WARNING)
logging.getLogger("telethon.network").setLevel(logging.WARNING)
