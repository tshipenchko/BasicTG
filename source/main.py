#new kernel
from colorama import Fore, Back, Style
import config 
from telethon import TelegramClient, sync
from telethon import events
import time
from random import randint
#config.py
api_id = config.api_id()
api_hash = config.api_hash()
#start client
client = TelegramClient('session_name', api_id, api_hash)
client.start()
@client.on(events.NewMessage(pattern='(?i).*ping'))
async def handler(event):
	await event.edit('Pong!')
@client.on(events.NewMessage(pattern='(?i).*fl'))
async def handler(event):
	a = 0
	while a <= 100:

		await event.edit(f'Loading {a}%')
		a +=1
	time.sleep(randint(1,2))
	await event.edit('Done!')
@client.on(events.NewMessage(pattern='(?i).*gay'))
async def handler(event):
	p = randint(0,100)
	await event.edit(f'🏳️‍🌈 I am {str(p)}% gay.')
client.run_until_disconnected()
