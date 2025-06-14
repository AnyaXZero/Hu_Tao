import time
import psutil  # Optional for system stats
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BANNED_USERS, SUPPORT_CHANNEL, SUPPORT_GROUP

# Initialize the Pyrogram Client
app = Client(
    "AnieXEricaMusic",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# Helper function to get system stats (optional)
async def get_system_stats():
    try:
        # Uptime
        uptime = time.time() - psutil.boot_time()
        uptime_str = f"{int(uptime // 3600)}h {int((uptime % 3600) // 60)}m"

        # CPU, RAM, Disk
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent

        return uptime_str, cpu, ram, disk
    except Exception:
        return "N/A", "N/A", "N/A", "N/A"

# Helper function to create inline keyboard
def get_inline_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Updates", url=SUPPORT_CHANNEL),
            InlineKeyboardButton("Support", url=SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton("Add to Group", url=f"https://t.me/{app.me.username.lstrip('@')}?startgroup=true"),
        ],
    ])

# Ping command handler
@app.on_message(filters.command(["ping", "status"]) & ~filters.user(BANNED_USERS))
async def ping_command(client: Client, message: Message):
    # Record start time
    start_time = time.time()

    # Send initial response
    response = await message.reply_text(f"🏓 Pinging {client.me.mention}...")

    # Measure Telegram API ping
    try:
        telegram_start = time.time()
        await client.get_me()  # Simple API call to measure latency
        telegram_ping = round((time.time() - telegram_start) * 1000, 2)  # Convert to ms
    except Exception:
        telegram_ping = "Error"

    # Get system stats (optional)
    uptime, cpu, ram, disk = await get_system_stats()

    # Calculate bot response time
    bot_ping = round((time.time() - start_time) * 1000, 2)  # Convert to ms

    # Format response
    ping_text = (
        f"🏓 **Pong!** {client.me.mention}\n"
        f"──────────────────\n"
        f"**Bot Ping**: {bot_ping} ms\n"
        f"**Telegram API Ping**: {telegram_ping} ms\n"
        f"**Uptime**: {uptime}\n"
        f"**CPU**: {cpu}%\n"
        f"**RAM**: {ram}%\n"
        f"**Disk**: {disk}%"
    )

    # Edit response with ping results and inline keyboard
    try:
        await response.edit_text(
            text=ping_text,
            reply_markup=get_inline_keyboard(),
            disable_web_page_preview=True
        )
    except Exception as e:
        await response.edit_text(f"Error updating message: {str(e)}")

# Run the bot
if __name__ == "__main__":
    app.run()
