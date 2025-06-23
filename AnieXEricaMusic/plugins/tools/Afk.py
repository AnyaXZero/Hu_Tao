from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app  # Use your actual bot/app instance
from datetime import datetime

# Store AFK data globally (you can later use DB for persistence)
AFK_USERS = {}
AFK_REASON = {}
AFK_TIME = {}

@app.on_message(filters.command("afk") & filters.me)
async def set_afk(_, message: Message):
    reason = " ".join(message.command[1:]) if len(message.command) > 1 else "ɪ'ᴍ ᴀꜰᴋ."
    user_id = message.from_user.id

    AFK_USERS[user_id] = True
    AFK_REASON[user_id] = reason
    AFK_TIME[user_id] = datetime.utcnow()

    await message.reply_text(f"ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴀꜰᴋ.\n📝 ʀᴇᴀꜱᴏɴ: {reason}")

@app.on_message(filters.text & filters.private | filters.group)
async def afk_reply(_, message: Message):
    if not message.from_user:
        return

    sender_id = message.from_user.id
    mentioned_users = [ent.user.id for ent in message.entities or [] if ent.type == "mention" or ent.type == "text_mention"]
    
    # Someone mentioned an AFK user
    for user_id in mentioned_users:
        if user_id in AFK_USERS and AFK_USERS[user_id]:
            reason = AFK_REASON.get(user_id, "AFK")
            since = AFK_TIME.get(user_id)
            afk_since = f"Since: {since.strftime('%Y-%m-%d %H:%M:%S')} UTC" if since else ""
            await message.reply_text(f"ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀꜰᴋ!\n📝 ʀᴇᴀꜱᴏɴ: {reason}\n{afk_since}")
            return

    # User sends message => they are no longer AFK
    if sender_id in AFK_USERS and AFK_USERS[sender_id]:
        AFK_USERS[sender_id] = False
        await message.reply_text(" ᴡᴇʟᴄᴏᴍᴇ ʙᴀᴄᴋ! ʏᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀꜰᴋ.")
