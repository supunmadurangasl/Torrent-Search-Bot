import os

TOKEN = os.environ.get("BOT_TOKEN")
API_HASH = os.environ.get("API_HASH")
API_ID = int(os.environ.get("API_ID"))
START_MESSAGE = os.environ.get("START_MESSAGE", "<b>Hi ! I am a simple torrent searcher by @Uvindu_Bro š±š°\n\n\nā¤ Made by @Uvindu_Bro š±š°</b>")
FOOTER_TEXT = os.environ.get("FOOTER_TEXT", "<b>~ Made by @UvinduBro š±š°</b>")
TORRENTS = {}
