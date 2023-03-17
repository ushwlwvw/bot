from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/68d2bbd94c43d14e848b4.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/68d2bbd94c43d14e848b4.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ZZZ7iZ")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/H_M_Dr")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5656828413").split()))


FAILED = "https://telegra.ph/file/68d2bbd94c43d14e848b4.jpg"
