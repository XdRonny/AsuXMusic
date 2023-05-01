from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQB1C26JiWymoM1DRAP5AbZsi0W1PYB8B6H4HZdJ9kqVLwBwr8KPuPbaotnqExMCJPCyZ9dwwFenQhsFPRBqdBlhQLO4RxTQ6V1EKu1uAS8U0y5zrXFo5BTh66K5afKN5QJaEeVJyS1k8XbxUpRnRnK-FJyZVlsRJOt7N-IYBmbsCmT3warcCk-nxNeqTsMkZ4UQmjcTqoDZUlahUfr8pY8UbAUbHgetuXfgjzyHNmV7RP-X4GwXdV07XmW6eJ3f_4gdY3CZWn6hQjsGhFEdwnqd0AC7GN61_S0Xe0ClipUvfh6LE6iS4baVNhhzB04ehAQL-1P9pkx2NuBFODGmHt5tAAAAAUfksOwA")

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
