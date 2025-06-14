from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app


@app.on_message(filters.left_chat_member)
async def goodbye(_, message: Message):
    user = message.left_chat_member

    # Optional: skip if a bot leaves
    if user.is_bot:
        return

    await message.reply_text(
        f" ɢᴏᴏᴅʙʏᴇ 👀, {user.mention}!\ɴʜᴏᴩᴇ ᴛᴏ ꜱᴇᴇ ʏᴏᴜ ᴀɢᴀɪɴ ꜱᴏᴍᴇᴅᴀʏ.!!"
    )
