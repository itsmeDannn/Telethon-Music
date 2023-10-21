import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6761376606:AAEo81S4Pj-QZQ4SLjS424jiLXBGAFwHCIs")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLcBu3W7ckrOLJyyk-EgLGO3L-4B2Aw-lZDuS5jbMV7CDvIP8FV9uk8Wg7DvXWTZRsDey7J6k5HIxjVznc08Wstd3Sv_DmsuFpFFwpy8W4pEIpIAw2_D8f8pOC7kFj_5VkMraCarvC3e94nYPi5tb7d6dtNOW4JoyAcZ7tSBkNRyDGd0fSbnhpTHEobEyCHlY8AXGCgVNRgC-rbnlZ1eahdkrTZxbXlCkJSc-5M1OXoTDL0BpjpXFbW1vQ2-P9mN-NaQyAIT4QT9cih9qu3cFZsAAJBMmlSarLGEn4sJ_0fahJY8iRO_KUu7_9QmeOrzCf3uxf_EgIgwFrr7mLp8ZH3P3Os=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "bandarmusikbot")
    SUPPORT = os.environ.get("SUPPORT", "bieunyy") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "asupanbieuny") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6253515673")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT'True) # Change it to "True"
