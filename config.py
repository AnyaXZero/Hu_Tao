import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "28235840"))
API_HASH = getenv("API_HASH", "b6d75900095294f59d32c9d7f04f3cfd")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7758662821:AAHMVvkI2CocuXAz-Y8NLQnxL-uTBK_hD9w")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Hutao:Hutaobot@cluster0.izwosfg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))
BOT_USERNAME = getenv("BOT_USERNAME", "shivang_mishra_op")
BOT_NAME = getenv("BOT_NAME", " 𝙼ᴜsɪᴄ˼ ♪")

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002567836754))

OWNER_ID = int(getenv("OWNER_ID", 7595051499))

OWNER = int(getenv("OWNER", 7595051499))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","hutao2")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-AA5DN1qAs5A9A42MDd_gRIvcP5e15YTpWZ8nXVvDsdNw_____wPkb01lB0Gk")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Zfini/Adonis",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = "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"
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/HutaoUpdates")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+C0s3qb7sRZA0ZjRk")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = '7f92897a59464ddbbf00f06cd6bda7fc'
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION","BQGu2EAAvMOD-sufBvFw-4pSkpZU0UB-H5q5JXMNhiRXXr7yiFgMUNHVy0ruYrxNHD3zwibTGcmGuBXPp24sEHVDPBETykiPAh9yaJERVk0THlZyv131R1LoPyRAzpdwpDy06hZ9aGJd5raTwzoYBgb_8xG2txRqlgSOq7LSsiBA1yJ3jU6IQrYNQ-lv0Ju1JI_PjHaf_OdIvzbbsz_MAmJcBQeJnobGHEMDUh5EMIrRHdPYNclLrxxDsJENeoFbG_3f5sMb8-lXDPmkhzd-pa9cvg7izy5D1alZ7k9rNpGDnB6-IpxH9gg2VdL1bHBotW1UlZXjuRHYMUv7bMf_N95K_H5Q6gAAAAG8798VAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL =  "https://files.catbox.moe/cw00x2.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/73ry0b.jpg"
STATS_IMG_URL = "https://files.catbox.moe/kwud6z.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/znrl3p.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/srf71g.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/917q6s.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/1kjxqg.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/r1ysgi.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/4odane.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/casi7g.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/0v9ldt.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
COMMAND_PREFIXES = ["/", "!", "."]
