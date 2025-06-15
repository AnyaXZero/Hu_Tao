from pyrogram import filters    
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery    
from AnieXEricaMusic import app    
    
# -------- Font Functions --------    
def bold(text):    
    return ''.join([chr(0x1D400 + ord(c) - 65) if 'A' <= c <= 'Z'    
                    else chr(0x1D41A + ord(c) - 97) if 'a' <= c <= 'z' else c for c in text])    
    
def italic(text):    
    return ''.join(['𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡'[ord(c)-65]    
                    if 'A' <= c <= 'Z' else    
                    '𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻'[ord(c)-97]    
                    if 'a' <= c <= 'z' else c for c in text])    
    
def mono(text):    
    return ''.join(['𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉'[ord(c)-65]    
                    if 'A' <= c <= 'Z' else    
                    '𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣'[ord(c)-97]    
                    if 'a' <= c <= 'z' else c for c in text])    
    
def cursive(text):    
    return ''.join(['𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩'[ord(c)-65]    
                    if 'A' <= c <= 'Z' else    
                    '𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃'[ord(c)-97]    
                    if 'a' <= c <= 'z' else c for c in text])    
    
def bubble(text):    
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    bubble = "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ" + "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ"    
    return ''.join([bubble[normal.index(c)] if c in normal else c for c in text])    
    
def smallcaps(text):    
    mapping = str.maketrans("abcdefghijklmnopqrstuvwxyz", "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ")    
    return text.translate(mapping)    
    
def doublestruck(text):    
    return ''.join([chr(0x1D538 + ord(c) - 65) if 'A' <= c <= 'Z'    
                    else chr(0x1D552 + ord(c) - 97) if 'a' <= c <= 'z' else c for c in text])    
    
def serif(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    serif_chars = "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑄𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁" + \
                  "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛"
    table = str.maketrans(normal, serif_chars)
    return text.translate(table)

def wide(text):    
    return ' '.join(c for c in text)    
    
def upside_down(text):    
    table = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",     
                          "ɐqɔpǝɟƃɥᴉɾʞʃɯuodbɹsʇnʌʍxʎz∀𐐒ƆᗡƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMXʎZ"[::-1])    
    return text[::-1].translate(table)    
    
# -------- Font Map --------    
style_map = {    
    "bold": bold,    
    "italic": italic,    
    "mono": mono,    
    "cursive": cursive,    
    "bubble": bubble,    
    "smallcaps": smallcaps,    
    "doublestruck": doublestruck,    
    "sans": sans,    
    "wide": wide,    
    "upside": upside_down,    
}    
    
# -------- Buttons --------    
def font_keyboard():    
    return InlineKeyboardMarkup([    
        [InlineKeyboardButton("𝐁 Bold", callback_data="font_bold"),    
         InlineKeyboardButton("𝘈 Italic", callback_data="font_italic"),    
         InlineKeyboardButton("𝙼 Mono", callback_data="font_mono")],    
        [InlineKeyboardButton("𝓒 Cursive", callback_data="font_cursive"),    
         InlineKeyboardButton("ⓑ Bubble", callback_data="font_bubble"),    
         InlineKeyboardButton("ꜱ Smallcaps", callback_data="font_smallcaps")],    
        [InlineKeyboardButton("𝔻 Double", callback_data="font_doublestruck"),    
         InlineKeyboardButton("𝗦 Sans", callback_data="font_sans"),    
         InlineKeyboardButton("W͟i͟d͟e", callback_data="font_wide")],    
        [InlineKeyboardButton("🔁 Upside", callback_data="font_upside"),    
         InlineKeyboardButton("🅰 Preview", callback_data="font_preview")]    
    ])    
    
# -------- Command Handler --------    
@app.on_message(filters.command(["font", "fonts"]))    
async def font_menu(_, message: Message):    
    if not message.reply_to_message or not message.reply_to_message.text:    
        return await message.reply("🔁 **Reply to a text message** to apply font style.")    
    
    await message.reply(    
        "**🎨 Choose a font style below:**",    
        reply_markup=font_keyboard()    
    )    
    
# -------- Callback Handler --------    
@app.on_callback_query(filters.regex(r"^font_"))    
async def font_callback(_, query: CallbackQuery):    
    if not query.message.reply_to_message or not query.message.reply_to_message.text:    
        return await query.answer("⚠️ Reply to a text message to style.", show_alert=True)    
    
    original_text = query.message.reply_to_message.text    
    action = query.data.split("_", 1)[1]    
    
    if action == "preview":    
        return await query.answer("🅰️ Just a preview button!")    
    
    styler = style_map.get(action)    
    if not styler:    
        return await query.answer("🚫 Unknown font style.")    
    
    styled_text = styler(original_text)    
    
    try:    
        await query.message.edit_text(    
            styled_text,    
            reply_markup=query.message.reply_markup    
        )    
    except Exception as e:    
        print(f"[❌ ERROR APPLYING STYLE] {e}")    
        await query.answer("❌ Failed to apply font style.")
