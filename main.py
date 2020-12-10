from telethon import TelegramClient, events, sync
import requests
import config





while True:

    cmd = input(">>>")
    try:
        client = TelegramClient('session_name', config.api_id(), config.api_hash())
        client.start()
    except ValueError:
        print('Unvalidated token')
        f = open('config.py','w')
        f.write("")

    if cmd == 'send':

        nick = input("nickname: ")

        inp = input('send: ')

        try:
            print(client.get_me().stringify())
            client.send_message(nick, inp)
        except ValueError:
            print('ERROR1: Ты не можешь отправлять сообщения самому себе')
