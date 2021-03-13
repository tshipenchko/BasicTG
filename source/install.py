import telethon
import colorama
from colorama import Fore, Back, Style
print(Fore.BLUE + ' ____            _     _____ ____')
print(Fore.BLUE + '| __ )  __ _ ___(_) __|_   _/ ___|')
print(Fore.BLUE + '|  _ \ / _` / __| |/ __|| || |  _')
print(Fore.YELLOW + '| |_) | (_| \__ \ | (__ | || |_| |')
print(Fore.YELLOW + '|____/ \__,_|___/_|\___||_| \____|\n\n')
print('')

ff = open('config.py', 'w')
ff.write("def api_id():\n  ")

ff.close()
#open #2
f = open('config.py', 'a')
#to config.py
print('If you enter data incorrectly, then there will be an error in main.py')

api_id = input(Fore.BLUE + 'api_id:' )
api_hash = input(Fore.BLUE + 'api_hash:' )
f.write('  api_id = ' +  api_id + '\n' + '    return api_id\n')
f.write('def api_hash():\n    api_hash =' + "'" + api_hash + "'" + '\n    return api_hash')
f.close()

print(Fore.GREEN + 'Succefuly installed. You need execute main.py')
