import random
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from AnieXEricaMusic import app

@app.on_message(filters.command(["gn", "n", "oodnight", "ood Night", "ood night"], prefixes=["/", "g", "G"]))
async def goodnight_command_handler(_, message: Message):
    sender = message.from_user
    sender_firstname = f"<a href='tg://user?id={sender.id}'>{sender.first_name}</a>"
    emoji = get_random_emoji()
    
    goodnight_phrases = [
        "sʟᴇᴇᴘ ᴛɪɢʜᴛ",
        "sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs",
        "ʀᴇsᴛ ᴡᴇʟʟ",
        "ʜᴀᴠᴇ ᴀ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs",
        "ʜᴀᴠᴇ ᴀ ᴘᴇᴀᴄᴇғᴜʟ ɴɪɢʜᴛ"
    ]
    
    goodnight_message = random.choice(goodnight_phrases)
    
    await message.reply_text(
        f"ɢᴏᴏᴅɴɪɢʜᴛ! {sender_firstname} {goodnight_message} {emoji}.",
        parse_mode=ParseMode.HTML
    )


def get_random_emoji():
    emojis = [
        "😴", "😪", "👀", "❤️", "✨", "🐼", "💤"
    ]
    return random.choice(emojis)


@app.on_message(filters.command(["gm", "m", "morning", "oodmorning", "ood morning"], prefixes=["/", "g", "G"]))
async def goodmorning_command_handler(_, message: Message):
    sender = message.from_user
    sender_firstname = f"<a href='tg://user?id={sender.id}'>{sender.first_name}</a>"
    emoji = get_random_emoji_for_morning()
    
    bot_private_link = f"<a href='tg://user?id={app.me.id}'>suzune"
    
    goodmorning_phrases = [
        "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ",
        "ʜᴀᴠᴇ ᴀ ɢʀᴇᴀᴛ ᴅᴀʏ",
        "ᴇɴᴊᴏʏ ᴛʜᴇ ɴᴇᴡ ᴅᴀʏ",
        "sᴛᴀʀᴛ ʏᴏᴜʀ ᴅᴀʏ ᴡɪᴛʜ ᴇɴᴇʀɢʏ",
        "ᴏᴘᴇɴ ʏᴏᴜʀ ᴇʏᴇs ᴀɴᴅ ʀᴇᴀʟɪᴢᴇ ʏᴏᴜ'ʀᴇ ᴀʟɪᴠᴇ"
    ]
    
    goodmorning_message = random.choice(goodmorning_phrases)
    
    await message.reply_text(
        f"{bot_private_link} ᴡɪsʜɪɴɢ ʏᴏᴜ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ!\n{sender_firstname} {goodmorning_message} {emoji}.",
        parse_mode=ParseMode.HTML
    )


def get_random_emoji_for_morning():
    emojis = [
        "😊", "❤️", "👀", "🕊️", "🌄", "💫", "✨", "💞"
    ]
    return random.choice(emojis)
