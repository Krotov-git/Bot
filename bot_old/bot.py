import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["geophone"])
def geophone(message):
    keyboard = types.ReplyKeyboardMarkup()
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id,
                     text="Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!",
                     reply_markup=keyboard)

# # на любую фразу пишет текст и предлогает перейти по ссылке
# #  но это можно делать и без команды а просто на условный текст
@bot.message_handler(commands=["dai"]) # комманда по которой будет предлогаться данная ссылка ниже
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru") # кнопка с сылкой и текстом
    keyboard.add(url_button)
    bot.send_message(message.chat.id,
                     "Привет! Нажми на кнопку и перейди в поисковик.",
                     reply_markup=keyboard) # тескст перед кнопкой и ссылкой

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    # bot.send_message(message.chat.id, message.text)  # если в методе оставить только эту строку то получится эхо бот, повторяет все что ты написал)
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Да я рад тебя видеть')
    if message.text == 'Ссылку':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на Яндекс",
                                                url="https://ya.ru")  # кнопка с сылкой и текстом
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

if __name__ == '__main__':
     bot.infinity_polling()