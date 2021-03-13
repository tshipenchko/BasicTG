#new kernel
from colorama import Fore, Back, Style
import config 
from telethon import TelegramClient, sync
#config.py
api_id = config.api_id()
api_hash = config.api_hash()
#start client
client = TelegramClient('session_name', api_id, api_hash)
client.start()
