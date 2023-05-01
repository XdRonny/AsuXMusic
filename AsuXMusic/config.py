from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQCbka9a1yC9OKcYTUF-Rlc2YIB76VwHx8b7DpKV8mCVwEiwmUofkLNSkSh-sskwJDi6eXkZhQ8le_XFNJNHoTjtVFodbNPemAMgm_PsDqGi6rq9SFkX2wo4evmEbm7R-4VttOhU7B9As-4G0FVqJfTY0W3quW4WEbX5yVISw8kAejEA_GTiFg4r6qYuQZnwqcOku1Lh1w83LGOJxQGAbv3ciOyBHaoGZ2g6mnzSvpA1WdN9Fw-3sJiVGV1_1CbQeborCPQHyjSCozlKBOwibGP6NW-cFh-KOLyq8v3Pp3U1OEMsB1oJ9oWrVNXo0NuDR_Sba9YvCKNNDOFAuQiZKFeqAAAAAUfksOwA")

BOT_TOKEN = getenv("BOT_TOKEN", "6170365487:AAGqlcCfjig6f_GKSnOnyYA6F9PdcRjSPvY")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BlackWorldMF")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheBothub")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6213690669").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6213690669").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/31e9ecee16a46575267a4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d744707634106cf76627a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
