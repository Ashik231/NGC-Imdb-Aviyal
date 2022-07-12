"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ഇപ്പോഴെലും വന്നു ഒന്നു ഞെക്കിയല്ലോ,സന്തോഷം ആയട മോനെ🙂,എന്നാലും ഇത്രെയും നാൾ നീ വന്നില്ലല്ലോ, എനിക് സങ്കടം ഒന്നും ഇല്ല എങ്കിലും ചെറിയൊരു ബിസമം🙃" 
REPO = "<b>Source ›› https://telegra.ph/file/e1f1ba863c82ab35e8a15.jpg</b>"
CHANNEL = "<b>Developer</b> ›› https://t.me/Unavailable4allTime\n\n<b>Owner ›› https://t.me/Unavailable4allTime</b>\n\n<b>Master Brain ›› https://t.me/Unavailable4allTime</b>"
NGC = "<b>Admin ›› https://t.me/Unavailable4allTime</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("ajax", COMMAND_HAND_LER) & f_onw_fliter)
async def ajax(_, message):
    await message.reply_text(AJAX)


