import base64
import httpx
import os
from pyrogram import filters
from AnieXEricaMusic import app
from pyrogram import filters
import pyrogram
from uuid import uuid4
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ParseMode

@app.on_message(filters.command(["stickerid", "stid"]))
async def sticker_id(app: app, msg):
    if not msg.reply_to_message:
        await msg.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ! 👀")        
    elif not msg.reply_to_message.sticker:
        await msg.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ !")        
    
    st_in = msg.reply_to_message.sticker
    sticker_id = f"<code>{st_in.file_id}</code>"
    unique_id = f"<code>{st_in.file_unique_id}</code>"
    
    await msg.reply_text(
        f"""
sᴛɪᴄᴋᴇʀ ɪɴғᴏ ❤️

sᴛɪᴄᴋᴇʀ ɪᴅ: {sticker_id}
sᴛɪᴄᴋᴇʀ ᴜɴɪǫᴜᴇ ɪᴅ: {unique_id}
""",
        parse_mode=ParseMode.HTML
    )
