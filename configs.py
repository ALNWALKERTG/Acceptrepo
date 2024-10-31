from os import path, getenv
import os, time 
#from pyrogram.types import BotCommand

class Config:
    API_ID = int(getenv("API_ID", "7679954"))
    API_HASH = getenv("API_HASH", "4af51af8f1a8b06ca2b076370ba93fba")
    BOT_TOKEN = getenv("BOT_TOKEN", "7344396275:AAFuEDN3U1v_1pboSapZFWEgy_-cXJVCglM")
    UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "CinemaKalavaraTG")
    UPDATECHANNEL_ID = int(getenv("UPDATECHANNEL_ID", "-1001514228365"))
    ADMIN = list(map(int, getenv("ADMIN", "7040444713 2144812475").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://hi:hi@auto.natzh.mongodb.net/?retryWrites=true&w=majority&appName=auto")
    LOG_CHANNEL = -1002439306214
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    DP_PIC = os.environ.get("DP_PIC", "https://envs.sh/_qj.mp4")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","TeamXo_Auto_Approve_Bot")
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://graph.org/file/67a5c787deb0d67fd3f69.jpg").split()

    LOGO = """🇩 🇵_🇧 🇴 🇹 🇿"""

dp1 = Config()
