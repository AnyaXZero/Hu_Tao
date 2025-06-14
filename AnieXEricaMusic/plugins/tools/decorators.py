# In AnieXEricaMusic/utils/decorators.py
from functools import wraps
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

def can_change_info(func):
    @wraps(func)
    async def wrapper(client, message: Message):
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        if user.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await func(client, message)
        return await message.reply_text("You need to be an admin to use this command.")
    return wrapper
