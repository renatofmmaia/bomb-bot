from .config import Config
import telegram

class TelegramBot:
    TOKEN = None
    CHAT_ID = None
    BOT = None
    ACTIVE = False
    
    def load_config():
        TelegramBot.TOKEN = Config.get('telegram','token')
        TelegramBot.CHAT_ID = Config.get('telegram','chat_id')
        
        if (TelegramBot.TOKEN and (TelegramBot.CHAT_ID and TelegramBot.CHAT_ID != 0)):
            TelegramBot.ACTIVE = True
        
        if TelegramBot.ACTIVE:
            TelegramBot.BOT = telegram.Bot(token=TelegramBot.TOKEN)
    
    def send_message_with_image(image_path: str, message: str = None):
        if TelegramBot.ACTIVE:
            if message:
                TelegramBot.send_message(message)
        
            TelegramBot.BOT.send_photo(chat_id=TelegramBot.CHAT_ID, photo=open(image_path, 'rb'))
        
    def send_message(message: str):
        if TelegramBot.ACTIVE:
            TelegramBot.BOT.send_message(chat_id=TelegramBot.CHAT_ID, text=message)
        