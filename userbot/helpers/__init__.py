# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from . import fonts
from . import memeshelper as arankmemes
from .aiohttp_helper import AioHttp
from .utils import *

flag = True
check = 0
while flag:
    try:
        from .chatbot import *
        from .functions import *
        from .memeifyhelpers import *
        from .progress import *
        from .qhelper import *
        from .tools import *
        from .utils import _arankutils, _format

        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break
