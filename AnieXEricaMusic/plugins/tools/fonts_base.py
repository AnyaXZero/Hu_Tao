from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app


@app.on_message(filters.left_chat_member)
async def goodbye(_, message: Message):
    name = message.left_chat_member.mention
    await message.reply_text(f"👀 {name} has left **{message.chat.title}**.\ɴᴡᴇ'ʟʟ ᴍɪꜱꜱ ʏᴏᴜ!")
