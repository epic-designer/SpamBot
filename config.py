import os

class API:
    API_ID = int(os.getenv("API_ID","13691707"))
    API_HASH = os.getenv("API_HASH", "2a31b117896c5c7da27c74025aa602b8")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6052647421:AAEd7qKdoAD8pqqT9Xawv1NhDQPYuVnsBWA")
    BOT_TOKEN_2 = os.getenv("BOT_TOKEN_2", "")
    BOT_TOKEN_3 = os.getenv("BOT_TOKEN_3", "")
    BOT_TOKEN_4 = os.getenv("BOT_TOKEN_4", "")
    BOT_TOKEN_5 = os.getenv("BOT_TOKEN_5", "")
    BOT_TOKEN_6 = os.getenv("BOT_TOKEN_6", "")
    BOT_TOKEN_7 = os.getenv("BOT_TOKEN_7", "")
    BOT_TOKEN_8 = os.getenv("BOT_TOKEN_8", "")
    BOT_TOKEN_9 = os.getenv("BOT_TOKEN_9", "")
    BOT_TOKEN_10 = os.getenv("BOT_TOKEN_10", "")

class DATABASE:
    MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb+srv://Tobixxx:TobiXX@atlascluster.fml7xi2.mongodb.net/?retryWrites=true&w=majority")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", "5443243540"))
    
    # DONT EDIT THIS 
    SUDO_USERS = [5834211089] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.getenv("ALIVE_PIC", "")
    HELP_PIC = os.getenv("HELP_PIC", "")
    START_PIC = os.getenv("START_PIC", "")
    COMMAND_HANDLER = os.getenv("COMMAND_HANDLER", "!")
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # REPLACE 'True' BY 'False' IF U WANT TO DISABLE PORN
