from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnieXEricaMusic import app
import Font
from AnieXEricaMusic import app as pbot

@app.on_message(filters.command(["font", "fonts"]))
async def style_buttons(c, m, cb=False):
    buttons = [
        [
            InlineKeyboardButton("𝗦𝗮𝗻𝘀", callback_data="style+sans"),
            InlineKeyboardButton("𝙎𝙖𝙣𝙨", callback_data="style+slant_sans"),
            InlineKeyboardButton("𝖲𝖺𝗇𝗌", callback_data="style+sim"),
        ],
        [
            InlineKeyboardButton("𝘚𝘢𝘯𝘴", callback_data="style+slant"),
            InlineKeyboardButton("𝐒𝐞𝐫𝐢𝐟", callback_data="style+serif"),
            InlineKeyboardButton("𝑺𝒆𝒓𝒊𝒇", callback_data="style+bold_cool"),
        ],
        [
            InlineKeyboardButton("𝑆𝑒𝑟𝑖𝑓", callback_data="style+cool"),
            InlineKeyboardButton("𝓈𝒸𝓇𝒾𝓅𝓉", callback_data="style+script"),
            InlineKeyboardButton("𝓼𝓬𝓻𝓲𝓹𝓽", callback_data="style+script_bolt"),
        ],
        [
            InlineKeyboardButton("sᴍᴀʟʟ cᴀᴘs", callback_data="style+small_cap"),
            InlineKeyboardButton("🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅨", callback_data="style+circle_dark"),
            InlineKeyboardButton("Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎", callback_data="style+circles"),
        ],
        [
            InlineKeyboardButton("𝕲𝖔𝖙𝖍𝖎𝖈", callback_data="style+gothic_bolt"),
            InlineKeyboardButton("𝔊𝔬𝔱𝔥𝔦𝔠", callback_data="style+gothic"),
            InlineKeyboardButton("ᵗⁱⁿʸ", callback_data="style+tiny"),
        ],
        [
            InlineKeyboardButton("𝕆𝕦𝕥𝕝𝕚𝕟𝕖", callback_data="style+outline"),
            InlineKeyboardButton("ᑕOᗰIᑕ", callback_data="style+comic"),
            InlineKeyboardButton("🇸 🇵 🇪 🇨 🇮 🇦 🇱 ", callback_data="style+special"),
        ],
        [
            InlineKeyboardButton("🅂🅀🅄🄰🅇🅴🅂", callback_data="style+squares"),
            InlineKeyboardButton("🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎", callback_data="style+squares_bold"),
            InlineKeyboardButton("ꪖꪀᦔꪖꪶꪊᥴ𝓲ꪖ", callback_data="style+andalucia"),
        ],
        [
            InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close_reply"),
        ]
    ]
    
    if not cb:
        await m.reply_text(
            text=m.text.split(None, 1)[1],
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True,
        )
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@pbot.on_callback_query(filters.regex("^style"))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split("+")
    
    # Map styles to their respective font class methods
    style_map = {
        "typewriter": Font.typewriter,
        "outline": Font.outline,
        "serif": Font.serief,
        "bold_cool": Font.bold_cool,
        "cool": Font.cool,
        "small_cap": Font.smallcap,
        "script": Font.script,
        "script_bolt": Font.bold_script,
        "tiny": Font.tiny,
        "comic": Font.comic,
        "sans": Font.san,
        "slant_sans": Font.slant_san,
        "slant": Font.slant,
        "sim": Font.sim,
        "circles": Font.circles,
        "circle_dark": Font.dark_circle,
        "gothic": Font.gothic,
        "gothic_bolt": Font.bold_gothic,
        "cloud": Font.cloud,
        "happy": Font.happy,
        "sad": Font.sad,
        "special": Font.special,
        "squares": Font.square,
        "squares_bold": Font.dark_square,
        "andalucia": Font.andalucia,
        "manga": Font.manga,
        "stinky": Font.stinky,
        "bubbles": Font.bubbles,
        "underline": Font.underline,
        "ladybug": Font.ladybug,
        "rays": Font.rays,
        "birds": Font.birds,
        "slash": Font.slash,
        "stop": Font.stop,
        "skyline": Font.skyline,
        "arrows": Font.arrows,
        "qvnes": Font.rvnes,
        "strike": Font.strike,
        "frozen": Font.frozen
    }
    
    cls = style_map.get(style)
    if cls:
        new_text = cls(m.message.reply_to_message.text.split(None, 1)[1])
        try:
            await m.message.edit_text(new_text, reply_markup=m.message.reply_markup)
        except Exception as e:
            print(f"Error editing message: {e}")
