from sample_config import Config
import os

class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", None))
    API_HASH = os.environ.get("API_HASH") or None
    # the name to display in your alive message
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    ALIVE_PIC = os.environ.get("ALIVE_PIC") or None
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = os.environ.get("DATABASE_URL", None)
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN") or os.environ.get(
        "TG_BOT_TOKEN_BF_HER", None
    )
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID", None))
    # command handler
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r".")
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r".")
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/CoderXKrishna/arankPlugins"
