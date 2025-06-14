import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import OWNER_ID, SUPPORT_CHAT, SUPPORT_CHANNEL
from Devine import app  # Ensure correct import name

@app.on_message(filters.command("alive"))
async def awake(_, message: Message):
    loading_1 = await message.reply_text("💖")
    await asyncio.sleep(0.5)

    loading_texts = ["<b>ʟᴏᴀᴅɪɴɢ</b>", "<b>ʟᴏᴀᴅɪɴɢ.</b>", "<b>ʟᴏᴀᴅɪɴɢ..</b>", "<b>ʟᴏᴀᴅɪɴɢ...</b>"]
    for text in loading_texts:
        await loading_1.edit_text(text)
        await asyncio.sleep(1)  
    await loading_1.delete()

    me = await app.get_me()
    owner = await app.get_users(OWNER_ID)

    if message.from_user.id == OWNER_ID:
        TEXT = "ɪ'ᴍ ᴀʟɪᴠᴇ ᴍʏ ʟᴏʀᴅ ⚡\n\n"
    else:
        TEXT = f"ʏᴏᴏ {message.from_user.mention}, ⚡\n\nɪ'ᴍ {me.mention}\n──────────────────\n"

    TEXT += f"ᴄʀᴇᴀᴛᴏʀ ⌯ {owner.mention}\n"
    TEXT += f"ᴠᴇʀsɪᴏɴ ⌯ 𝟸.𝟷𝟼 ʀx\n"
    TEXT += f"ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ⌯ 𝟹.𝟷𝟸.𝟶\n"
    TEXT += f"ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ ⌯ 𝟸.𝟶.𝟷𝟶𝟼"

    BUTTON = [
        [
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=SUPPORT_CHANNEL),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="ᴀᴅᴅ ɪɴ ɢʀᴏᴜᴘ", url=f"https://t.me/{me.username}?startgroup=true"),
        ],
    ]    
    
    await message.reply_text(text=TEXT, reply_markup=InlineKeyboardMarkup(BUTTON))
