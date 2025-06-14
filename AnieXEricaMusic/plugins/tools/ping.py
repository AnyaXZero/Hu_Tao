import time
import platform
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnieXEricaMusic import app
import pyrogram

BOT_START_TIME = time.time()

# Customize these
SUPPORT_GROUP = "https://t.me/+C0s3qb7sRZA0ZjRk"
SUPPORT_CHANNEL = "https://t.me/HutaoUpdates"
PING_IMAGE_URL = "https://files.catbox.moe/jnkll9.jpg"  # Change if needed

@app.on_message(filters.command("ping"))
async def ping(_, message: Message):
    start = time.time()
    temp = await message.reply_text("🏓 Pinging...")
    ping_ms = int((time.time() - start) * 1000)

    python_version = platform.python_version()
    pyrogram_version = pyrogram.__version__
    uptime = format_time(int(time.time() - BOT_START_TIME))

    await temp.delete()

    caption = (
        " ɪ'ᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ 🦋✨\n"
        
        "🏓 ᴩᴏɴɢ!\n"
        f"➤ ᴩɪɴɢ : {ping_ms}ms\n"
        f"➤ ᴩʏᴛʜᴏɴ : {python_version}\n"
        f"➤ ᴩʏʀᴏɢʀᴀᴍ : {pyrogram_version}\n"
        f"➤ ᴜᴩᴛɪᴍᴇ : {uptime}"
    )

    await message.reply_photo(
        photo=PING_IMAGE_URL,
        caption=caption,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("ꜱᴜᴩᴩᴏʀᴛ", url=SUPPORT_GROUP),
                InlineKeyboardButton("ᴜᴩᴅᴀᴛᴇꜱ", url=SUPPORT_CHANNEL),
            ]
        ])
    )


def format_time(seconds):
    mins, sec = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    time_parts = []
    if days: time_parts.append(f"{days}d")
    if hours: time_parts.append(f"{hours}h")
    if mins: time_parts.append(f"{mins}m")
    if sec or not time_parts: time_parts.append(f"{sec}s")
    return " ".join(time_parts)
