from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app

@app.on_message(filters.new_chat_members)
async def welcome(_, message: Message):
    for member in message.new_chat_members:
        if member.is_bot:
            continue  # skip bots
        await message.reply_text(
            f"ʜᴇʏ ᴡᴇʟᴄᴏᴍᴇ, {member.mention}!\nᴡᴇ'ʀᴇ ɢʟᴀᴅ ᴛᴏ ʜᴀᴠᴇ ʏᴏᴜ ʜᴇʀᴇ 🎉"
        )
