import asyncio
import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions


from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


python = 'https://sun9-48.userapi.com/impg/vsAJ7_aFnIxuke26MduWuhMh0twgxr9BOtiSxg/mnGX4J0GhB4.jpg?size=1200x675&quality=96&proxy=1&sign=97ed1ffe5e5fc43a348406da36a708f8&type=album'


# Команда приветствия, первое что получает пользователь при нажтие на кнопку старт в начале диалога
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет!', reply_markup=kb.greet_kb)


# команда помощи, выводит список возможных команд бота
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/voice', '/photo', '/group', '/note', '/file, /testpre', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


# команды вызывающие кнопки...в процессе понимания..
@dp.message_handler(commands=['hi6'])
async def process_hi6_command(message: types.Message):
    await message.reply("Шестое - запрашиваем контакт и геолокацию\n"
                        "Эти две кнопки не зависят друг от друга",
                        reply_markup=kb.markup_request)


# Команда которая может выводить определенный набор фото или других медиа файлов (при модификации ее), но нужно разобраться с БД и путями
@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    caption = 'Это питон, язык на котором я написан! :eyes:'
    await bot.send_photo(message.from_user.id, python,
                         caption=emojize(caption),
                         reply_to_message_id=message.message_id)


# Обработчик текста, помещается в самом конце, ибо я еще не допер до конца, реагирует на ввод пользователя
@dp.message_handler(content_types=['text'])
async def unknown_message(msg: types.Message):
    # если пользователь вводит что то из приведенного слева
    if msg.text == ('Привет! 👋') or msg.text == ('привет') or msg.text == ('Привет'):
        # Бот ему отвечает эту фразу
        message_text = text(bold('Меня зовут Питонатор! И да, у моего создателя плохо с фантазией, но родителей мы не выбираем! Вот список доступных команд!'),
                            '/voice', '/photo', '/group', '/note', '/file', sep='\n')
        await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)
    # В случае если то что пишет пользователь не попадает ни под один вариант
    else:
        message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
                            italic('\nЯ просто напомню,'), 'что есть',
                            code('команда'), '/help') # Бот ответит вот это
        await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp)