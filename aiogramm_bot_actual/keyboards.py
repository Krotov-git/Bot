from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# это так называемая шаблонная кнопка, то что н ней написано то и будет выводиться
# первой строкой мы создаем сам обьект кнопки, и то что она в себе несет
# второй строкой используя метод адд мы добавили обьекту ReplyKeyboardMarkup кнопку которую создали в первой строке
# в скобках у обьекта указали параметры: 1-делает нашу кнопку маленькой и красивой, 2-скрывет кнопку после нажатия на нее
button_hi = KeyboardButton('Привет! 👋')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi)
#----------------------------------------------------------------------------------------------


#------------------------------------
button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')
#-----------------------------------


# Метод add принимает в себя любое количество кнопок,
# всегда начинает добавление с новой строки и переносит ряд при достижении значения установленной ширины.
markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)


# Метод row тоже принимает любое количество,
# но при этом не переносит кнопки на новый ряд, а добавляет всё полученное в одну строчку.
markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3)


# Метод insert работает по схеме схожей с add, но только начинает добавлять к последнему ряду.
# И только если там уже достигнута максимальная ширина, начинает новую строку.
# Взглянем на него ещё раз при создании следующей клавиатуры.
markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button4, button5)
markup5.insert(button6)
#-----------------------------------------------

# кнопки геолокации и телефона
markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)
#------------------------------------------------------------------------


markup_big = ReplyKeyboardMarkup()

markup_big.add(
    button1, button2, button3, button4, button5, button6
)
markup_big.row(
    button1, button2, button3, button4, button5, button6
)

markup_big.row(button4, button2)
markup_big.add(button3, button2)
markup_big.insert(button1)
markup_big.insert(button6)
markup_big.insert(KeyboardButton('9️⃣'))



# Пройдёмся по строчкам по порядку, чтобы не осталось вопросов:
#
# мы создаём клавиатуру типа InlineKeyboardMarkup, указываем,
# что ширина строки должна быть не больше двух (напомню, что это не распространяется на метод row)
# и сразу добавляем туда уже готовую кнопку
# далее добавляем кнопку, у которой указываем другие данные в параметре callback_data
# следом генерируем три новые кнопки и добавляем их дважды. Сначала методом add, затем через row.
# И так как ширина клавиатуры равна двум, то в первом случае происходит перенос третьей кнопки, во втором случае нет
# затем добавляем кнопки, у которых указываем уже не callback_data, а другие параметры.
# То, что мы добавим в switch_inline_query, будет автоматически использовано при нажатии кнопки:
# пользователю предложат выбрать чат, а там вызовется инлайн режим этого бота
# (в поле ввода сообщения добавится юзернейм бота), следом через пробел будет прописано то,
# что мы указали. Параметр может принимать пустую строку, тогда инлайн режим запустится без какого-либо запроса,
# но если будет указан текст, то он и добавится
# при использовании switch_inline_query_current_chat произойдёт ровно то же, что и в предыдущем пункте,
# но без выбора чата, а запустится в текущем (было сложно догадаться по названию, я знаю)
# ну и последний параметр url - добавляем ссылку на внешний ресурс, либо диплинк в самом Телеграме
# Так как параметр клавиатуры row_width равен двум, то кнопки автоматически расставились соответствующе.
# Рассмотрим реакцию на кнопки по порядку: При нажатии первой срабатывает наш первый колбек, так как не важно,
# в какую клавиатуру добавлена кнопка, важно, какая у неё callback_data ☝️.
# Поэтому добавлять инлайн кнопку можно сколько угодно раз в любые инлайн клавиатуры.
# Кнопки со второй по пятую имеют схожую структуру в callback_data, поэтому внутри хэндлера проверяем,
# какой код у нажатой кнопки и:
# если 2, то отвечаем на запрос и передаем информационное сообщение. Аргумент text это текст ответа на запрос.
# По умолчанию он будет показан вверху чата и сам скроется через пару секунд.
# если 5, то отвечаем так же, но указываем show_alert=True, таким образом мы сообщаем клиенту,
# что нужно показать окошко с текстом
# в ином случае просто отвечаем на колбек
inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)

inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='btn2'))
inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')

inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)

inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
inline_kb_full.add(InlineKeyboardButton('Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/'))