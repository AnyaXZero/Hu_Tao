import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
import ffmpeg
from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app

# Command for memes
@app.on_message(filters.command("mmf"))
async def mmf(_, message: Message):
    chat_id = message.chat.id
    reply_message = message.reply_to_message

    if len(message.text.split()) < 2:
        return await message.reply_text("**Please provide text.**\nUsage: `/mmf Top Text;Bottom Text`")

    if not reply_message or not (reply_message.photo or (reply_message.document and reply_message.document.mime_type.startswith("image/"))):
        return await message.reply_text("**Please reply to an image (e.g., JPG, PNG).**")

    msg = await message.reply_text("❄️ Creating your meme...")

    text = message.text.split(None, 1)[1]
    file = await app.download_media(reply_message)

    meme = await drawText(file, text, is_sticker=False)
    if meme:
        await app.send_document(chat_id, document=meme)
        os.remove(meme)
    else:
        await message.reply_text("⚠️ Failed to create meme. Please try again.")

    await msg.delete()

# Command for static stickers
@app.on_message(filters.command("sticker"))
async def sticker(_, message: Message):
    chat_id = message.chat.id
    reply_message = message.reply_to_message

    if len(message.text.split()) < 2:
        return await message.reply_text("**Please provide text.**\nUsage: `/sticker Top Text;Bottom Text`")

    if not reply_message or not (reply_message.photo or (reply_message.document and reply_message.document.mime_type.startswith("image/"))):
        return await message.reply_text("**Please reply to an image (e.g., JPG, PNG).**")

    msg = await message.reply_text("❄️ Creating your sticker...")

    text = message.text.split(None, 1)[1]
    file = await app.download_media(reply_message)

    sticker_file = await drawText(file, text, is_sticker=True)
    if sticker_file:
        await app.send_sticker(chat_id, sticker=sticker_file)
        os.remove(sticker_file)
    else:
        await message.reply_text("⚠️ Failed to create sticker. Ensure the image is valid and under 350KB.")

    await msg.delete()

# Command for animated stickers
@app.on_message(filters.command("animatedsticker"))
async def animated_sticker(_, message: Message):
    chat_id = message.chat.id
    reply_message = message.reply_to_message

    if len(message.text.split()) < 2:
        return await message.reply_text("**Please provide text.**\nUsage: `/animatedsticker Top Text;Bottom Text`")

    if not reply_message or not (
        reply_message.video or (reply_message.document and reply_message.document.mime_type.startswith("video/")) or
        (reply_message.document and reply_message.document.mime_type == "image/gif")
    ):
        return await message.reply_text("**Please reply to a video or GIF (e.g., MP4, GIF).**")

    msg = await message.reply_text("❄️ Creating your animated sticker...")

    text = message.text.split(None, 1)[1]
    file = await app.download_media(reply_message)

    sticker_file = await create_animated_sticker(file, text)
    if sticker_file:
        await app.send_sticker(chat_id, sticker=sticker_file)
        os.remove(sticker_file)
    else:
        await message.reply_text("⚠️ Failed to create animated sticker. Ensure the video/GIF is valid and under 350KB.")

    await msg.delete()

# Command for GIFs
@app.on_message(filters.command("gif"))
async def gif(_, message: Message):
    chat_id = message.chat.id
    reply_message = message.reply_to_message

    if len(message.text.split()) < 2:
        return await message.reply_text("**Please provide text.**\nUsage: `/gif Top Text;Bottom Text`")

    if not reply_message or not (
        reply_message.photo or
        reply_message.video or
        (reply_message.document and (reply_message.document.mime_type.startswith("image/") or reply_message.document.mime_type == "image/gif"))
    ):
        return await message.reply_text("**Please reply to an image, video, or GIF.**")

    msg = await message.reply_text("❄️ Creating your GIF...")

    text = message.text.split(None, 1)[1]
    file = await app.download_media(reply_message)

    gif_file = await create_gif(file, text)
    if gif_file:
        await app.send_animation(chat_id, animation=gif_file)
        os.remove(gif_file)
    else:
        await message.reply_text("⚠️ Failed to create GIF. Please try again.")

    await msg.delete()

async def drawText(image_path, text, is_sticker=False):
    try:
        img = Image.open(image_path).convert("RGBA" if is_sticker else "RGB")
    except Exception:
        if os.path.exists(image_path):
            os.remove(image_path)
        return None
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)

    i_width, i_height = img.size

    # Resize for stickers (one side must be 512px)
    if is_sticker:
        if i_width > i_height:
            new_width = 512
            new_height = int((512 / i_width) * i_height)
        else:
            new_height = 512
            new_width = int((512 / i_height) * i_width)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    i_width, i_height = img.size
    font_size = min(int((70 / 640) * i_width), int(i_height / 10))

    # Font path
    if os.name == "nt":
        fnt_path = "arial.ttf"
    else:
        fnt_path = "./Alya/assets/default.ttf"

    try:
        m_font = ImageFont.truetype(fnt_path, font_size)
    except OSError:
        m_font = ImageFont.load_default()

    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    wrap_width = max(20, i_width // 40)

    upper_text, lower_text = text.split(";", 1) if ";" in text else (text, "")

    def draw_outline_text(draw, position, text, font, fill_color="white"):
        x, y = position
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            draw.text((x + dx, y + dy), text, font=font, fill="black")
        draw.text((x, y), text, font=font, fill=fill_color)

    if upper_text:
        for line in textwrap.wrap(upper_text, width=wrap_width):
            uwl, uht, uwr, uhb = m_font.getbbox(line)
            u_width, u_height = uwr - uwl, uhb - uht
            draw_outline_text(
                draw,
                ((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                line,
                m_font,
            )
            current_h += u_height + pad

    if lower_text:
        for line in textwrap.wrap(lower_text, width=wrap_width):
            uwl, uht, uwr, uhb = m_font.getbbox(line)
            u_width, u_height = uwr - uwl, uhb - uht
            draw_outline_text(
                draw,
                ((i_width - u_width) / 2, i_height - u_height - int((20 / 640) * i_width)),
                line,
                m_font,
            )

    output_file = "memify.webp" if is_sticker else "memify.png"
    img.save(output_file, "WEBP" if is_sticker else "PNG", quality=85 if is_sticker else 100)

    # Check file size for stickers (max 350KB)
    if is_sticker and os.path.getsize(output_file) > 350 * 1024:
        return None

    return output_file

async def create_animated_sticker(input_file, text):
    try:
        # Convert input to WebM with text overlay using ffmpeg
        output_file = "animated_sticker.webm"
        stream = ffmpeg.input(input_file)
        stream = ffmpeg.filter(stream, "scale", 512, -1)  # Scale to 512px on one side
        stream = ffmpeg.filter(stream, "fps", fps=30)  # Set reasonable FPS
        stream = ffmpeg.filter(
            stream,
            "drawtext",
            fontfile="arial.ttf" if os.name == "nt" else "./Alya/assets/default.ttf",
            text=text.replace(";", "\n") if ";" in text else text,
            fontsize=40,
            fontcolor="white",
            shadowcolor="black",
            shadowx=2,
            shadowy=2,
            x="(w-text_w)/2",
            y="(h-text_h)/2"
        )
        stream = ffmpeg.output(stream, output_file, c_v="libvpx-vp9", b_v="256k", t=3, format="webm")
        ffmpeg.run(stream)

        # Check file size (max 350KB)
        if os.path.getsize(output_file) > 350 * 1024:
            return None

        return output_file
    except Exception:
        if os.path.exists(input_file):
            os.remove(input_file)
        return None

async def create_gif(input_file, text):
    try:
        output_file = "output.gif"
        if input_file.lower().endswith((".mp4", ".mov", ".webm")):
            # Convert video to GIF with text overlay
            stream = ffmpeg.input(input_file)
            stream = ffmpeg.filter(stream, "scale", 512, -1)
            stream = ffmpeg.filter(
                stream,
                "drawtext",
                fontfile="arial.ttf" if os.name == "nt" else "./Alya/assets/default.ttf",
                text=text.replace(";", "\n") if ";" in text else text,
                fontsize=40,
                fontcolor="white",
                shadowcolor="black",
                shadowx=2,
                shadowy=2,
                x="(w-text_w)/2",
                y="(h-text_h)/2"
            )
            stream = ffmpeg.output(stream, output_file, format="gif")
            ffmpeg.run(stream)
        else:
            # Single image to GIF
            img = Image.open(input_file).convert("RGB")
            img = await drawText(input_file, text, is_sticker=False)
            Image.open(img).save(output_file, "GIF")

        # Check file size (aim for < 8MB for Telegram)
        if os.path.getsize(output_file) > 8 * 1024 * 1024:
            return None

        return output_file
    except Exception:
        if os.path.exists(input_file):
            os.remove(input_file)
        return None

__mod_name__ = "mmf, sticker, animatedsticker & gif"
