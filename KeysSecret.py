"""
If you are deploying it locally then follow following steps:
Remove all the thing after = sign except in category part.
Pass the values directly i.e. without using quotaion where int is written.
Pass the value in C like "First Second Third" make sure you seprate them using space.
"""


from os import getenv

API_ID = int(getenv("API_ID", 26959103))
API_HASH = getenv("API_HASH", "ebe24f37c6f8ee727fc406c68ba5bc70")
BOT_TOKEN = getenv("BOT_TOKEN", "6204804430:AAGoMvBeD9Fz_rJ7G4v5tYw4-CzcUgtc0rY")
DB_URI = getenv("mongodb+srv://Anshul0554:Anshul0554@cluster0.uwx7fnj.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = getenv("luster0")
OWNER = int(getenv(5657873637))
SUDO = list({int(i) for i in getenv(5657873637)})
OWNER_ID = ["5657218265"]
OWNER_ID.append(OWNER)               
OWNER_ID.extend(SUDO)
C = getenv("CATEGORY").split(None) # Don't remove this line
x = []
for i in C:
    x.append(i.strip().lower())
COIN_NAME = str(getenv("Bounty"))
COIN_EMOJI = getenv("฿")
CATEGORY = x
AMOUNT = int(getenv("AMOUNT", 5000))
CHAT_ID = int(getenv(-655759304))
PREMIUM_CHANNEL = int(getenv(-655759304))
PREMIUM_COST = int(getenv(10, 50))
