from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
from AnieXEricaMusic import app
import httpx
import re
import html


async def get_manga_info(manga_name):
    url = 'https://graphql.anilist.co'
    query = '''
    query ($manga: String) {
      Media (search: $manga, type: MANGA) {
        id
        title {
          romaji
          english
          native
        }
        description(asHtml: false)
        chapters
        volumes
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
    variables = {"manga": manga_name}
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
    return html.escape(desc.strip())


@app.on_message(filters.command("manga"))
async def manga_info(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ Please provide a manga name.\n\nExample: `/manga One Piece`",
            parse_mode=ParseMode.MARKDOWN
        )

    manga_name = " ".join(message.command[1:])
    result, error = await get_manga_info(manga_name)

    if not result:
        return await message.reply_text(
            error or "❌ Manga not found.",
            parse_mode=ParseMode.MARKDOWN
        )

    # Extract info
    title = result['title']['romaji']
    english = result['title'].get('english')
    native = result['title']['native']
    chapters = result.get('chapters', 'N/A')
    volumes = result.get('volumes', 'N/A')
    status = result.get('status', 'N/A')
    score = result.get('averageScore', 'N/A')
    desc = clean_description(result.get('description'))
    image = result['coverImage']['large']
    site_url = result['siteUrl']

    # Optional buttons
    character_url = None
    sequel_url = None

    if result.get("characters", {}).get("edges"):
        character_url = result["characters"]["edges"][0]["node"]["siteUrl"]

    for rel in result.get("relations", {}).get("edges", []):
        if rel["relationType"] == "SEQUEL":
            sequel_url = rel["node"]["siteUrl"]
            break

    short_desc = desc[:800] + "..." if len(desc) > 800 else desc
    short_desc = f"<code>{short_desc}</code>"

    english_line = f"📘 <b>Title (English):</b> <code>{english}</code>\n" if english else ""

    caption = (
        f"📚 <b>Title (Romaji):</b> <code>{title}</code>\n"
        f"{english_line}"
        f"🈶 <b>Title (Native):</b> <code>{native}</code>\n"
        f"📄 <b>Chapters:</b> <code>{chapters}</code>\n"
        f"📦 <b>Volumes:</b> <code>{volumes}</code>\n"
        f"📊 <b>Score:</b> <code>{score}/100</code>\n"
        f"📌 <b>Status:</b> <code>{status}</code>\n\n"
        f"📝 <b>Description:</b>\n{short_desc}"
    )

    buttons = [
        [
            InlineKeyboardButton("Description", url=site_url),
            InlineKeyboardButton("Characters", url=character_url)
            if character_url else InlineKeyboardButton("Characters", callback_data="no_characters"),
        ],
        [
            InlineKeyboardButton("Manga Page", url=site_url),
            InlineKeyboardButton("Sequel", url=sequel_url)
            if sequel_url else InlineKeyboardButton("Sequel", callback_data="no_sequel"),
        ]
    ]

    await message.reply_photo(
        photo=image,
        caption=caption,
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(buttons)
  )
