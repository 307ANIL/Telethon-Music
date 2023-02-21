import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6127157269:AAH8S6KRBiWaZ9MgIN7SV6r_-JIgMSMoxrM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKEBu4qULZYO2KB2w4J6kvXWuMELgyz3IP7TQ_7brQ-JL5ew6QncZwBUfqFIFIXY2UCIQW1JnmswBkceouutBloIP_wc2VTqL2QVQmReua4mSiVHPnZf6kfpBVTJnCgpLFMCIB3QS9yApLP_uianMqn_eTXMT2PyKzl6g1kLNdCjrXgACzxtS3TiFUIKGfthPm8ee5dBRbVV8Qk_-gKHOmoezxq49cDjwQKWlVYUFYAEZfFKlUqwP8q2LABct6o63RqmTCrlakO40jTqGNCE2LBJvaT54TnGar4Gxqa7TzSiL2dO7pDNTLPoSKt2ec-IscxE6heyWfTh7erRjMBI1VKLlV4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
