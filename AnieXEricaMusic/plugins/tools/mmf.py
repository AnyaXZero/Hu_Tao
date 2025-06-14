import os
import textwrap
import uuid
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app

from moviepy.editor import VideoFileClip
import lottie
import cairosvg


@app.on_message(filters.command("mmf"))
async def mmf(_, message: Message):
    chat_id = message.chat.id
    reply_message = message.reply_to_message

    if len(message.text.split()) < 2:
        return await message.reply_text(
            "**Please provide meme text.**\nUsage: `/mmf Top Text;Bottom Text`"
        )

    if not reply_message:
        return await message.reply_text("**Please reply to an image, sticker, or GIF.**")

    # Check if media is valid
    is_valid = (
        reply_message.photo
        or reply_message.sticker
        or reply_message.animation
        or (reply_message.document and reply_message.document.mime_type and reply_message.document.mime_type.startswith(("image/", "video/", "application/x-tgsticker")))
    )

    if not is_valid:
        return await message.reply_text("**Unsupported media. Reply to an image, sticker, or GIF.**")

    msg = await message.reply_text("❄️ Processing...")

    text = message.text.split(None, 1)[1]
    raw_file = await app.download_media(reply_message)
    converted_image = None

    try:
        # Handle static stickers and images directly
        if reply_message.photo or (reply_message.sticker and reply_message.sticker.is_static):
            converted_image = raw_file

        # Handle animated stickers (.tgs)
        elif reply_message.sticker and reply_message.sticker.is_animated:
            converted_image = await convert_tgs_to_png(raw_file)

        # Handle video stickers (.webm)
        elif reply_message.sticker and reply_message.sticker.is_video:
            converted_image = await extract_frame(raw_file)

        # Handle animations and gifs
        elif reply_message.animation or (reply_message.document and reply_message.document.mime_type.startswith("video/")):
            converted_image = await extract_frame(raw_file)

        if not converted_image or not os.path.exists(converted_image):
            return await msg.edit_text("❌ Failed to process media.")

        meme = await draw_text(converted_image, text)
        if not meme.endswith(".webp"):
            return await msg.edit_text(meme)

        await app.send_document(chat_id, meme)

    except Exception as e:
        await msg.edit_text(f"❌ Error: {e}")
    finally:
        await msg.delete()
        for f in [raw_file, converted_image, meme]:
            if f and os.path.exists(f):
                os.remove(f)


async def extract_frame(video_path):
    output_path = f"/tmp/{uuid.uuid4().hex}.jpg"
    clip = VideoFileClip(video_path)
    clip.save_frame(output_path, t=0.5)
    return output_path


async def convert_tgs_to_png(tgs_path):
    output_path = f"/tmp/{uuid.uuid4().hex}.png"
    try:
        with open(tgs_path, "rb") as f:
            animation = lottie.parsers.tgs.parse_tgs(f.read())
        svg = animation.render_frame(0)
        cairosvg.svg2png(bytestring=svg, write_to=output_path)
        return output_path
    except Exception as e:
        return None


async def draw_text(image_path, text):
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception:
        return "❌ Couldn't open the image."

    i_width, i_height = img.size
    fnt_path = "arial.ttf" if os.name == "nt" else "./Alya/assets/default.ttf"

    try:
        m_font = ImageFont.truetype(fnt_path, int((70 / 640) * i_width))
    except OSError:
        return "⚠️ Font not found."

    upper_text, lower_text = (text.split(";", 1) + [""])[:2]
    draw = ImageDraw.Draw(img)
    wrap_width = max(20, i_width // 40)
    pad = 5

    def draw_outline(draw, pos, line, font):
        x, y = pos
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            draw.text((x + dx, y + dy), line, font=font, fill="black")
        draw.text((x, y), line, font=font, fill="white")

    current_h = 10
    for line in textwrap.wrap(upper_text, width=wrap_width):
        bbox = m_font.getbbox(line)
        u_width, u_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw_outline(draw, ((i_width - u_width) / 2, current_h), line, m_font)
        current_h += u_height + pad

    if lower_text:
        lines = textwrap.wrap(lower_text, width=wrap_width)
        total_height = sum([m_font.getbbox(line)[3] - m_font.getbbox(line)[1] + pad for line in lines])
        current_y = i_height - total_height - int((20 / 640) * i_width)
        for line in lines:
            bbox = m_font.getbbox(line)
            u_width, u_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            draw_outline(draw, ((i_width - u_width) / 2, current_y), line, m_font)
            current_y += u_height + pad

    output_file = f"/tmp/{uuid.uuid4().hex}.webp"
    img.save(output_file, "webp")
    return output_file


__mod_name__ = "mmf"
