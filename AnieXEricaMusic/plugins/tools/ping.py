import time
from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app  # your bot instance

@app.on_message(filters.command("ping"))
async def ping(_, message: Message):
    start = time.time()
    reply = await message.reply_text("🏓 Pinging...")
    end = time.time()
    ping_time = (end - start) * 1000
    await reply.edit_text(f"🏓 Pong!\n`{int(ping_time)}ms`")
