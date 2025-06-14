import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app


@app.on_message(filters.command("mmf"))
async def mmf(_, message: Message):
    chat_id = message.chat.id
    reply_message = message.reply_to_message

    if len(message.text.split()) < 2:
        return await message.reply_text("**Please provide some text.**\nUsage: `/mmf Top Text;Bottom Text`")

    if not reply_message or not (reply_message.photo or reply_message.document):
        return await message.reply_text("**Please reply to an image to create a meme.**")

    msg = await message.reply_text("❄️ Creating your meme...")

    text = message.text.split(None, 1)[1]
    file = await app.download_media(reply_message)

    meme = await drawText(file, text)
    await app.send_document(chat_id, document=meme)

    await msg.delete()
    os.remove(meme)


async def drawText(image_path, text):
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception:
        return "Couldn't open the image."
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)

    i_width, i_height = img.size

    # Font path
    if os.name == "nt":
        fnt_path = "arial.ttf"  # Make sure this exists on Windows
    else:
        fnt_path = "./AnieXEricaMusic/assets/font.ttf"  # Linux font path

    try:
        m_font = ImageFont.truetype(fnt_path, int((70 / 640) * i_width))
    except OSError:
        return "⚠️ Font file not found! Please check your font path."

    # Split the input text
    if ";" in text:
        upper_text, lower_text = text.split(";", 1)
    else:
        upper_text = text
        lower_text = ""

    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    wrap_width = max(20, i_width // 40)

    def draw_outline_text(draw, position, text, font):
        x, y = position
        # Black outline
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            draw.text((x + dx, y + dy), text, font=font, fill="black")
        draw.text((x, y), text, font=font, fill="white")

    # Draw top text
    if upper_text:
        for line in textwrap.wrap(upper_text, width=wrap_width):
            uwl, uht, uwr, uhb = m_font.getbbox(line)
            u_width, u_height = uwr - uwl, uhb - uht
            draw_outline_text(
                draw,
                (((i_width - u_width) / 2), int((current_h / 640) * i_width)),
                line,
                m_font,
            )
            current_h += u_height + pad

    # Draw bottom text
    if lower_text:
        for line in textwrap.wrap(lower_text, width=wrap_width):
            uwl, uht, uwr, uhb = m_font.getbbox(line)
            u_width, u_height = uwr - uwl, uhb - uht
            draw_outline_text(
                draw,
                (
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                line,
                m_font,
            )
            current_h += u_height + pad

    webp_file = "memify.webp"
    img.save(webp_file, "webp")

    return webp_file


__mod_name__ = "mmf"
