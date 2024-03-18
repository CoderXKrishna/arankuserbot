from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 24049626
    API_HASH = "680a4153538eb9f9a2195cbcb464114f"
    # the name to display in your alive message
    ALIVE_NAME = "Arank"
    ALIVE_PIC = "https://te.legra.ph/file/a1a30607889f3e983c830.jpg"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://zzbexnvo:ZvxGk16w9KAryc-upU2hSDQW7nLbmBWl@cornelius.db.elephantsql.com/zzbexnvo"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOKcBu6TvY_j12l5pXKoYlEFKpGOwg3zbrkVqUhXKIwFu5NEFu5WBkIANXrQ0x2Cm6GIHjKjyPqQ82qGVVJbjz1aF1rU-dBOMqgcbmXUz1g586meHYfMNWTNeK_ltXQYVi_E9isSalTIaubTBuQ6AhL0feNerPL6iztAEyKnc94gzCOlghcdgaCbccGG4dNHtOia3pcujucRyTpQa1ixZCo4S0ZHmc2_VPrlW3IyhXf7RXVmEXI9qtHauwQZjz1oH8a_wgtkv83RnR7XMnibDoOhdHWqKqeiKVz_HgYsYUd4YwyfYTyOzBwMBMbDJRAj8Xskdrm9gjdGLt_5Vv-C5F-MctNs="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "7015417253:AAEuQT0BoyO34BHijFCuchiU6RzACZTbKFk"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002101729420
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/CoderXKrishna/arankPlugins"
