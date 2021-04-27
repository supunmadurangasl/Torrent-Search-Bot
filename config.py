import os

TOKEN = os.environ.get("BOT_TOKEN")
API_HASH = os.environ.get("API_HASH")
API_ID = int(os.environ.get("API_ID"))
START_MESSAGE = os.environ.get("START_MESSAGE", "<b>Hi ! I am a simple torrent searcher by @Uvindu_Bro 🇱🇰\n\n\n❤ Made by @Uvindu_Bro 🇱🇰</b>")
FOOTER_TEXT = os.environ.get("FOOTER_TEXT", "<b>~ Made by @UvinduBro 🇱🇰</b>")
TORRENTS = {}
