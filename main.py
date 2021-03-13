#new kernel
from colorama import Fore, Back, Style
import config 
from telethon import TelegramClient, sync

api_id = config.api_id()
api_hash = congig.api_hash()

client = TelegramClient('session_name', api_id, api_hash)
client.start()
