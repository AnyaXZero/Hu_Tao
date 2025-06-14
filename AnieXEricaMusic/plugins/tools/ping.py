import time
import platform
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app
import pyrogram

# Optional: Track bot start time for uptime
BOT_START_TIME = time.time()

@app.on_message(filters.command("ping"))
async def ping(_, message: Message):
    start = time.time()
    reply = await message.reply_text("🏓 Pinging...")
    end = time.time()
    ping_ms = int((end - start) * 1000)

    python_version = platform.python_version()
    pyrogram_version = pyrogram.__version__

    uptime_sec = int(time.time() - BOT_START_TIME)
    uptime = format_time(uptime_sec)

    await reply.edit_text(
        f"🏓 **ᴩᴏɴɢ!**\n"
        f"➤ **ᴩɪɴɢ:** `{ping_ms}ms`\n"
        f"➤ **ᴩʏᴛʜᴏɴ:** `{python_version}`\n"
        f"➤ **ᴩʏʀᴏɢʀᴀᴍ:** `{pyrogram_version}`\n"
        f"➤ **ᴜᴩᴛɪᴍᴇ:** `{uptime}`"
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
