from pyrogram import Client, filters  
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton  
from pyrogram.enums import ParseMode  
from AnieXEricaMusic import app  
import httpx  
import re  
  
  
async def get_anime_info(anime_name):  
    url = 'https://graphql.anilist.co'  
    query = '''  
    query ($anime: String) {  
      Media (search: $anime, type: ANIME) {  
        id  
        title {  
          romaji  
          english  
          native  
        }  
        description(asHtml: false)  
        episodes  
        status  
        averageScore  
        coverImage {  
          large  
        }  
        siteUrl  
        characters(perPage: 1) {  
          edges {  
            node {  
              name {  
                full  
              }  
              siteUrl  
            }  
          }  
        }  
        relations {  
          edges {  
            relationType  
            node {  
              title {  
                romaji  
              }  
              siteUrl  
            }  
          }  
        }  
      }  
    }  
    '''  
    variables = {"anime": anime_name}  
    async with httpx.AsyncClient(timeout=10.0) as client:  
        try:  
            response = await client.post(url, json={'query': query, 'variables': variables})  
            data = response.json()  
            if 'errors' in data:  
                return None, f"❌ Error: {data['errors'][0]['message']}"  
            return data['data']['Media'], None  
        except Exception as e:  
            return None, f"❌ Request failed: {e}"  
  
  
def clean_description(desc):  
    if not desc:  
        return "No description available."  
    desc = re.sub(r"<br\s*/?>", "\n", desc)  
    desc = re.sub(r"<[^>]+>", "", desc)  
    return desc.strip()  
  
  
@app.on_message(filters.command("anime"))  
async def anime_info(client: Client, message: Message):  
    if len(message.command) < 2:  
        return await message.reply_text(  
            "❌ Please provide an anime name.\n\nExample: `/anime Naruto`",  
            parse_mode=ParseMode.MARKDOWN  
        )  
  
    anime_name = " ".join(message.command[1:])  
    result, error = await get_anime_info(anime_name)  
  
    if not result:  
        return await message.reply_text(  
            error or "❌ Anime not found.",  
            parse_mode=ParseMode.MARKDOWN  
        )  
  
    # Extracting fields  
    title = result['title']['romaji']  
    english = result['title'].get('english')  
    native = result['title']['native']  
    episodes = result.get('episodes', 'N/A')  
    status = result.get('status', 'N/A')  
    score = result.get('averageScore', 'N/A')  
    desc = clean_description(result.get('description'))  
    image = result['coverImage']['large']  
    site_url = result['siteUrl']  
  
    # Optional character and sequel buttons  
    character_url = None  
    sequel_url = None  
  
    if result.get("characters", {}).get("edges"):  
        character_url = result["characters"]["edges"][0]["node"]["siteUrl"]  
  
    for rel in result.get("relations", {}).get("edges", []):  
        if rel["relationType"] == "SEQUEL":  
            sequel_url = rel["node"]["siteUrl"]  
            break  
  
    # Description in mono  
    short_desc = desc[:800] + "..." if len(desc) > 800 else desc  
    short_desc = f"`{short_desc}`"  # monospaced description  
  
    english_line = f"🇺🇸 Title (English): `{english}`\n" if english else ""  
  
    caption = (  
        f"🎌 Title (Romaji): `{title}`\n"  
        f"{english_line}"  
        f"🈶 Title (Native): `{native}`\n"  
        f"📺 Episodes: `{episodes}`\n"  
        f"📊 Score: `{score}/100`\n"  
        f"📌 Status: `{status}`\n\n"  
        f"📝 Description:\n{short_desc}"  
    )  
  
    buttons = [  
        [  
            InlineKeyboardButton("Description", url=site_url),  
            InlineKeyboardButton("Characters", url=character_url) if character_url else InlineKeyboardButton("Characters", callback_data="no_characters"),  
        ],  
        [  
            InlineKeyboardButton("Series List", url=site_url),  
            InlineKeyboardButton("Sequel", url=sequel_url) if sequel_url else InlineKeyboardButton("Sequel", callback_data="no_sequel"),  
        ]  
    ]  
  
    await message.reply_photo(  
        photo=image,  
        caption=caption,  
        parse_mode=ParseMode.MARKDOWN,  
        reply_markup=InlineKeyboardMarkup(buttons)  
    )
