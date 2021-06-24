import asyncio
import time

from telethon import version
from userbot.utils import admin_cmd, sudo_cmd

from LUCIFER import ALIVE_NAME, StartTime, lionver
from LUCIFER.helper import functions as dcdef 
from LUCIFER.LUCIFERConfig import Config, Var

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓυcιғεя x υsεя"

# Thanks to Sipak bro and Aryan..
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
# modded for Lion X Userbot
# now in LUCIFERUSERBOT

global fuk
fuk = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/73373552e9217e010e853.jpg"
""" =======================CONSTANTS====================== """
# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "ℓυcιғεя ʊֆɛʀɮօȶ ɨֆ օռʟɨռɛ!"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else "https://telegra.ph/file/73373552e9217e010e853.jpg"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#

@Lion.on(admin_cmd(pattern=r"alive"))
@Lion.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def hmm(yes):
    await yes.get_chat()
    global fuk
    fuk = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - StartTime))
    pm_caption = f"〢**{CUSTOM_ALIVE}**\n\n"
    pm_caption += "〢**Mʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɢ**\n\n"
    pm_caption += "〢 Aʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ ✗\n\n"
    pm_caption += f"〢 **LUCIFER 𝙑𝙀𝙍𝙎𝙄𝙊𝙉**: `{LUCIFERver}`\n"
    pm_caption += f"〢 **𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 𝙑𝙀𝙍𝙎𝙄𝙊𝙉** ☞ {version.__version__}\n"
    pm_caption += "〢 **𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝘾𝙃𝘼𝙉𝙉𝙀𝙇** ☞ [ᴊᴏɪɴ](https://t.me/LUCIFER_SUPPORT_CHANNEL)\n"
    pm_caption += "〢 **𝙇𝙄𝘾𝙀𝙉𝙎𝙀**  ☞ [𝚃𝙴𝙰𝙼 LUCIFER 𝚄𝙱](https://github.com/kaal0408)\n"
    pm_caption += (
        "〢 **𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔** ☞ [𝙻𝙸𝙾𝙽 𝚄𝙱](https://github.com/teamLUCIFER/LUCIFER-USERBOT)\n\n"
    )
    pm_caption += f"〢 **LUCIFER 𝙐𝙋𝙏𝙄𝙈𝙀** ☞ {uptime}\n\n"
    pm_caption += f"〢 **𝙈𝙔 𝙋𝙀𝙍𝙊 𝙈𝘼𝙎𝙏𝙀𝙍** ☞ [{DEFAULTUSER}](tg://user?id={fuk})\n"
    on = await borg.send_file(
        yes.chat_id, file=ALV_PIC, caption=pm_caption, link_preview=False
    )

# This Alive is for Lion X modded from dc 
# use with credits
