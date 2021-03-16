#new kernel
from colorama import Fore, Back, Style
import config 
from telethon import TelegramClient, sync
from telethon import events
import time
from random import randint
import os 
#import modules

#config.py
api_id = config.api_id()
api_hash = config.api_hash()
#start client
client = TelegramClient('session_name', api_id, api_hash)
client.start()



@client.on(events.NewMessage(pattern='(?i).*restart'))
async def handler(event):
	try:
		await event.edit(f'Restarting... ')
		time.sleep(randint(1,2))
		await event.edit(f'Restart succefully!')
		os.abort()
	except:
		await event.edit(f'Restart failed!')

@client.on(events.NewMessage(pattern='(?i).*install'))
async def handler(event):
	replied = await event.get_reply_message()
	module_text = 'hello world!'
	file = open('main.py','r')
	file_read = file.read()
	text = file_read.replace('','')
	file.close()
	file = open('main.py','w')
	file.write(text)
	file.close()
	file = open('main.py','a')
	file.write(module_text)
	file.write('\n')
	await event.respond(f' {replied}')
	await event.edit('Module installed!')
	os.abort()

@client.on(events.NewMessage(pattern='(?i).*ping'))
async def handler(event):

	await event.edit('Pong!')


client.run_until_disconnected()
