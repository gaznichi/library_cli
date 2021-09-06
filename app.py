from admin import admin_panel
from models import create_table
from guest import guest_panel
import logging

logging.basicConfig(level = logging.INFO, filename = 'library.log')

logging.info("Started")
create_table()
who = input('''
Здравствуйте
Добро пожаловать на Library App 0.0.1

Для начала представьтесь 
вы кто

1. Администратор
2. Гость(Visitor)
''')

if who == '1':
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    if username == 'admin' and password == 'admin':
        admin_panel()
    else:
        print('Неправильное имя пользователя или пароль')
    
elif who == '2':
    print('Добро пожаловать в библиотеку')
    guest_panel()
