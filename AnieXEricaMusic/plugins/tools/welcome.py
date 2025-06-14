from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnieXEricaMusic import app


@app.on_message(filters.new_chat_members)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        name = member.mention if not member.is_bot else f"🤖 {member.first_name}"

        await message.reply_text(
            text=f"ʜᴇʏ ᴡᴇʟᴄᴏᴍᴇ 🌷 {name} to **{message.chat.title}**!\nʜᴀᴠᴇ ᴀ ɢʀᴇᴀᴛ ᴛɪᴍᴇ ʜᴇʀᴇ 🦋✨",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("ʜᴇʟᴩ", callback_data="ʜᴇʟᴩ")],
                ]
            )
        )
