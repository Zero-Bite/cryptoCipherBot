from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types.input_file import InputFile
from itertools import cycle
import time

from auto_data import TOKEN
import markups as nav
import states as st

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Привествие - выход на главное меню
@dp.message_handler(commands=['start'])
async def hello(message: types.Message):

    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAED1c5iAAEcqoPSpKKYQvXm07PXc8wZrmcAAhkAA1m7_CWtc4ylGlCTryME")

    time.sleep(0)

    await bot.send_message(message.chat.id, f"Приветствую тебя, {message.from_user.username} !\n"
                                            f"этот бот был создан с целью ускорения обучения криптографии и упрощения рутинной работы зашифровки и дешифровки сообщений,"
                                            f" а так же для популяризации направления криптографии 🙃\n"
                                            f"Если у тебя возникнут вопросы по работе бота или ты заметил ошибки в его работе, то обращайся за помощью --- /help", reply_markup=nav.first_plane_menu)


# Поддержка:
@dp.message_handler(commands=['help'])
async def help(message: types.Message):

    await bot.send_message(message.chat.id, "Если ты перешел в этот раздел, то скорее всего что-то не так в работе бота, но перед тем как делать такие выводы убедись, что ты выполняешь "
                                            "все правила использования каждого шифра 😡\n", reply_markup=nav.back_menu)

    time.sleep(1)

    my_name = '@found_map'

    await bot.send_message(message.chat.id, f"В случае если ошибка не решена напиши мне {my_name}")

# обработчики команд из главного меню

# Информация/Справка
@dp.message_handler(Text(equals="ℹ️ InFo ℹ️"))
async def send_information(message: types.Message):

    await message.reply("Бот 'Study_Crypto' включает в себя 3 метода шифрования:\n1 - Обратный шифр\n2 - Шифр Цезаря\n3 - Шифр Виженера\n"
                        "Поскольку каждый из этих шифров алфавитный, то в них представлен выбор алфавита 😉\nКак дополнение к каждому шифру есть пояснение 👾\n"
                        "Перед использованием обратитесь к правилам, хорошего пользования !", reply_markup=nav.info_menu)

# Раздел шифрования
@dp.message_handler(Text(equals="🔐 Шифры 🔐"))
async def ciphers(message: types.Message):

    await message.reply("🔐 Шифры 🔐", reply_markup=nav.second_plane_menu_ciphers)

# Перехоим в меню Шифр Вижера
@dp.message_handler(Text(equals="Шифр Вижера"))
async def visher(message: types.Message):

    photo = InputFile(r"vizhener.png")


    await bot.send_photo(message.chat.id, photo=photo, caption="Шифр Виженера состоит из последовательности нескольких шифров Цезаря с различными значениями сдвига. "
                        "Для зашифровывания может использоваться таблица алфавитов, называемая tabula recta или квадрат (таблица) Виженера. "
                        "Применительно к латинскому алфавиту таблица Виженера составляется из строк по 26 символов, причём каждая следующая строка сдвигается на несколько позиций. "
                        "Таким образом, в таблице получается 26 различных шифров Цезаря", reply_markup=nav.thrird_plane_menu_under_reverse_ciphers)


@dp.message_handler(Text(equals="Подробнее об ученом 👨‍🏫"))
async def about_vizher(message: types.Message):

    await bot.send_message(message.chat.id, "Блез де Виженер (фр. Blaise de Vigenère; 5 апреля 1523, Сен-Пурсен-сюр-Сиуль — 19 февраля 1596, Париж) — французский дипломат, криптограф и алхимик. \n"
                                            "Некоторые люди считают, что изобретение шифра, называемого в настоящее время шифром Виженера, в XIX веке было ошибочно приписано именно ему.\n"

"Давид Кан в своей книге «Взломщики кодов», написал: «история проигнорировала важный факт и назвала шифр именем Виженера, несмотря на то, что он ничего не сделал для его создания».\n"

"Однако это неправда.\nВ своём трактате 1585 года он описал шифр, подобный шифру Тритемия, однако изменил систему выбора конкретного шифра замены для каждой буквы.\nОдной из предложенных техник было использование букв другого открытого текста для выбора ключа каждой буквы исходного текста.\n"

"Описанный шифр известен как шифр Виженера и, при длине случайного ключа, равной длине открытого текста, является абсолютно стойким шифром, что было математически доказано много позже (в XX веке в работах Шеннона)", reply_markup=nav.back_menu)


# Шифр Вижера зашифровать
@dp.message_handler(Text(equals="Шифр Вижера: Зашифровать"))
async def visher_encrypt_en(message: types.Message):

    await bot.send_message(message.chat.id, "Выберите язык", reply_markup=nav.language_vizher_menu)


@dp.callback_query_handler(text="reverse_ciphers_encrypt_inline_en")
async def back_get_vizhers(call: types.CallbackQuery):

    await bot.send_message(call.message.chat.id, "Введите ваше сообщение состоящее ТОЛЬКО из букв англисского языка(без пробелов и знаков пунктуации)", reply_markup=nav.back_menu)

    await st.vizhers_encypt.ciesar_encrypt_eng_mess.set()

@dp.message_handler(state=st.vizhers_encypt.ciesar_encrypt_eng_mess)
async def get_mess_to_vizh(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['vizher_message'] = str(message.text)

        await bot.send_message(message.chat.id, "🔑 Введите сообщение на англисском которое будет являться ключом для кодировки,"
                                                "состоящее ТОЛЬКО из букв англисского языка\n(без пробелов и знаков пунктуации) 🔑", reply_markup=nav.back_menu)

        await st.vizhers_encypt.ciesar_encrypt_eng_shift.set()

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

@dp.message_handler(state=st.vizhers_encypt.ciesar_encrypt_eng_shift)
async def get_shift_vizhr(message: types.Message, state: FSMContext):
    try:


        async with state.proxy() as data:
            data['shift_decrypt'] = str(message.text)


        data = await state.get_data()


        vizher_message = data.get("vizher_message").lower()

        vizher_shift = data.get("shift_decrypt").lower()

        from itertools import cycle

        alp = 'abcdefghijklmnopqrstuvwxyz'

        def encode_vijn(text, key):
            f = lambda arg: alp[(alp.find(arg[0]) + alp.find(arg[1]) % 26) % 26]
            return ''.join(map(f, zip(text, cycle(key))))

        def decode_vijn(coded_text, key):
            f = lambda arg: alp[alp.find(arg[0]) - alp.find(arg[1]) % 26]
            return ''.join(map(f, zip(coded_text, cycle(key))))

        text = vizher_message
        key = vizher_shift


        str_3 = (encode_vijn(text, key))

        await state.finish()

        await bot.send_message(message.chat.id,
                               f"Ваше слово: {vizher_message}\n"
                               f"Ваш ключ: {vizher_shift}\n"
                               f"Результат шифрования: {str_3}\n"
                               f"Если есть вопросы обратитесь к справке 🎮",
                               reply_markup=nav.back_menu)

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

# Шифр Вижера расшифровать
@dp.message_handler(Text(equals="Шифр Вижера: Расшифровать"))
async def visher_decrypt_en(message: types.Message):

    await bot.send_message(message.chat.id, "Шифр Вижера: Расшифровать", reply_markup=nav.language_vizher_menu_decrypt)


@dp.callback_query_handler(text="reverse_ciphers_decrypt_inline")
async def decrypt_visher_get_mess(call: types.CallbackQuery):

    await bot.send_message(call.message.chat.id, "Введите ваше сообщение состоящее ТОЛЬКО из букв англисского языка\n(без пробелов и знаков пунктуации)", reply_markup=nav.back_menu)

    await st.vizhers_decrypt.ciesar_decrypt_eng_mess.set()

@dp.message_handler(state=st.vizhers_decrypt.ciesar_decrypt_eng_mess)
async def mess_to_decrypr_get(message: types.Message, state: FSMContext):
    try:

        async with state.proxy() as data:
            data['message_decrypt'] = str(message.text)

        await bot.send_message(message.chat.id, "🔑 Введите сообщение на англисском которое будет являться ключом для кодировки,"
                                                "состоящее ТОЛЬКО из букв англисского языка\n(без пробелов и знаков пунктуации) 🔑", reply_markup=nav.back_menu)


        await st.vizhers_decrypt.ciesar_decrypt_eng_shift.set()

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

@dp.message_handler(state=st.vizhers_decrypt.ciesar_decrypt_eng_shift)
async def get_shift_to_vizher(message: types.Message, state: FSMContext):

    try:

        async with state.proxy() as data:
            data['shift_decrypt'] = str(message.text)


        data = await state.get_data()


        vizher_message = data.get("message_decrypt").lower()

        vizher_shift = data.get("shift_decrypt")

        from itertools import cycle

        alp = 'abcdefghijklmnopqrstuvwxyz0'

        def encode_vijn(text, key):
            f = lambda arg: alp[(alp.find(arg[0]) + alp.find(arg[1]) % 26) % 26]
            return ''.join(map(f, zip(text, cycle(key))))

        def decode_vijn(coded_text, key):
            f = lambda arg: alp[alp.find(arg[0]) - alp.find(arg[1]) % 26]
            return ''.join(map(f, zip(coded_text, cycle(key))))

        text = vizher_message
        key = vizher_shift


        str_3 = (decode_vijn(text, key))

        await state.finish()

        await bot.send_message(message.chat.id,
                               f"Ваше слово: {vizher_message}\n"
                               f"Ваш ключ: {vizher_shift}\n"
                               f"Результат расшифрования: {str_3}\n"
                               f"Если есть вопросы обратитесь к справке 🎮",
                               reply_markup=nav.back_menu)

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()


    '''
    Переходим в меню Обратный шифр
    '''

@dp.message_handler(Text(equals="Шифр Атбаша"))
async def revers(message: types.Message):

    photo = InputFile(r'atbash.jpg')

    await bot.send_photo(message.chat.id, photo=photo, caption="Самый-самый простой шифр.\nЕго суть – переворот алфавита с ног на голову.\n"

    "Например, есть у нас алфавит, который полностью соответствует обычной латинице.\n"

    "Для реализации шифра Атбаша просто инвертируем его.\n«А» станет «Z», «B» превратится в «Y» и наоборот.\n", reply_markup=nav.fifth_plane_menu_under_vizher_ciphers)

# Обратный шифр зашифровать / англисский
@dp.message_handler(Text(equals="Шифр Атбаша: Зашифровать"), state=None)
async def revers_encrypt_en(message: types.Message):

    await bot.send_message(message.chat.id, "Выберите язык сообщения", reply_markup=nav.language_menu)


@dp.callback_query_handler(text="english_revers_encrypt")
async def your_language(call: types.CallbackQuery):

    await bot.send_message(call.message.chat.id, "Введите слово/слова на англиском языке которое хотите зашифровать\n(без пробелов и знаков пунктуации)",
                           reply_markup=nav.back_menu)

    await st.reverse_cipher_encrypt.reverse_cipher_encrypt_english.set()

@dp.message_handler(state=st.get_language.what_language_revers_encrypt) # Работа с машиной состояний
async def encrypt_rev_engl_get_message(message: types.Message, state: FSMContext):


    await st.reverse_cipher_encrypt.reverse_cipher_encrypt_english.set()

@dp.message_handler(state=st.reverse_cipher_encrypt.reverse_cipher_encrypt_english)
async def encryt_revers_engl(message: types.Message, state: FSMContext):

    try:
        answer_message = message.text

        await state.update_data(answer_message_1=answer_message)

        data = await state.get_data()

        answer_message_1 = data.get("answer_message_1").upper()


        encrypt = ''

        dict = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',

                        'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',

                        'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',

                        'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',

                        'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}

        for letter in answer_message_1:
            if (letter != ' '):
                encrypt += dict[letter]
            else:
                encrypt += ' '

        await state.finish()

        # await call.message.answer(f"Результат шифрования: {cipher}\nЕсли есть вопросы обратитесь к справке 🎮")
        await message.answer(
            f"Вы ввели сообщение: {answer_message_1}\nРезультат шифрования: {encrypt}\nЕсли есть вопросы обратитесь к справке 🎮",
            reply_markup=nav.back_menu)

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()


# Обратный шифр зашифровать / русский
@dp.callback_query_handler(text="russian_revers_encrypt")
async def revers_encrypt_rus(call: types.CallbackQuery):

    await bot.send_message(call.message.chat.id, "Введите слово/слова на русском языке которое хотите зашифровать\n(без пробелов и знаков пунктуации)",
                           reply_markup=nav.back_menu)

    await st.reverse_cipher_encrypt.reverse_cipher_encrypt_russian.set()

@dp.message_handler(state=st.reverse_cipher_encrypt.reverse_cipher_encrypt_russian)
async def encrypt_rev_ru(message: types.Message, state: FSMContext):

    try:

        answer_message = message.text

        await state.update_data(answer_message_1=answer_message)

        data = await state.get_data()

        answer_message_1 = data.get("answer_message_1").upper()

        encrypt = ''

        dict = {'А': 'Я', 'Б': 'Ю', 'В': 'Э', 'Г': 'Ь', 'Д': 'Ы',

                        'Е': 'Ъ', 'Ж': 'Щ', 'З': 'Ш', 'И': 'Ч',

                        'Й': 'Ц', 'К': 'Х', 'Л': 'Ф', 'М': 'У', 'Н': 'Т',

                        'О': 'С', 'П': 'Р', 'Р': 'П', 'С': 'О', 'Т': 'Н',

                        'У': 'М', 'Ф': 'Л', 'Х': 'К', 'Ц': 'Й', 'Ч': 'И', 'Ш': 'З', 'Щ': 'Ж', 'Ъ': 'Е', 'Ы': 'Д', 'Ь': 'Г',
                        'Э': 'В', 'Ю': 'Б', 'Я': 'А'}

        for letter in answer_message_1:
            if (letter != ' '):
                encrypt += dict[letter]
            else:
                encrypt += ' '

        await state.finish()

        await message.answer(
            f"Вы ввели сообщение: {answer_message_1}\nРезультат шифрования: {encrypt}\nЕсли есть вопросы обратитесь к справке 🎮",
            reply_markup=nav.back_menu)


    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()




# Обратный шифр расшифровать / англисский
@dp.message_handler(Text(equals="Шифр Атбаша: Расшифровать"), state=None)
async def revers_decrypt_en(message: types.Message):

    await bot.send_message(message.chat.id, "Выберите язык сообщения", reply_markup=nav.language_menu)

@dp.callback_query_handler(text="english_revers_decrypt", state=None)
async def get_language_to_rev_decrypt(call: types.CallbackQuery):

    await bot.send_message(call.message.chat.id, "Введите слово/слова на англиском языке которое хотите расшифровать\n(без пробелов и знаков пунктуации)",
                           reply_markup=nav.back_menu)

    await st.reverse_cipher_dectypt.reverse_cipher_dectypt_english.set()

@dp.message_handler(state=st.reverse_cipher_dectypt.reverse_cipher_dectypt_english)# Работа с машиной состояний
async def decrypt_rev_eng(message: types.Message, state: FSMContext):

    try:
        answer = message.text

        await state.update_data(decrypt_eng_answer=answer)

        data = await state.get_data()

        decrypt_eng_answer = data.get("decrypt_eng_answer").upper()

        decrypt_eng_answer.upper()

        dict = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',

                        'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',

                        'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',

                        'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',

                        'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}

        decrypt = ''

        for letter in decrypt_eng_answer:
            if (letter != ' '):
                decrypt += dict[letter]
            else:
                decrypt += ' '

        await state.finish()

        # await call.message.answer(f"Результат шифрования: {cipher}\nЕсли есть вопросы обратитесь к справке 🎮")
        await message.answer(f"Вы ввели сообщение: {decrypt_eng_answer}\nРезультат дешифровки: {decrypt}\nЕсли есть вопросы обратитесь к справке 🎮", reply_markup=nav.back_menu)


    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

# Обратный шифр расшифровать / русский
@dp.callback_query_handler(text="russian_revers_decrypt")
async def decrypt_rev_rus_get_message(call: types.CallbackQuery):

    await bot.send_message(call.message.chat.id, "Введите слово/слова на русском языке которое хотите расшифровать\n(без пробелов и знаков пунктуации)",
                           reply_markup=nav.back_menu)

    await st.reverse_cipher_dectypt.reverse_cipher_dectypt_russian.set()

@dp.message_handler(state=st.reverse_cipher_dectypt.reverse_cipher_dectypt_russian)
async def decrypt_rev_rus(message: types.Message, state: FSMContext):

    try:

        answer = message.text

        await state.update_data(decrypt_eng_answer=answer)

        data = await state.get_data()

        decrypt_eng_answer = data.get("decrypt_eng_answer").upper()

        decrypt_eng_answer.upper()

        dict = {'А': 'Я', 'Б': 'Ю', 'В': 'Э', 'Г': 'Ь', 'Д': 'Ы',

                        'Е': 'Ъ', 'Ж': 'Щ', 'З': 'Ш', 'И': 'Ч',

                        'Й': 'Ц', 'К': 'Х', 'Л': 'Ф', 'М': 'У', 'Н': 'Т',

                        'О': 'С', 'П': 'Р', 'Р': 'П', 'С': 'О', 'Т': 'Н',

                        'У': 'М', 'Ф': 'Л', 'Х': 'К', 'Ц': 'Й', 'Ч': 'И', 'Ш': 'З', 'Щ': 'Ж', 'Ъ': 'Е', 'Ы': 'Д', 'Ь': 'Г',
                        'Э': 'В', 'Ю': 'Б', 'Я': 'А'}

        decrypt = ''

        for letter in decrypt_eng_answer:
            if (letter != ' '):
                decrypt += dict[letter]
            else:
                decrypt += ' '

        await state.finish()

        # await call.message.answer(f"Результат шифрования: {cipher}\nЕсли есть вопросы обратитесь к справке 🎮")
        await message.answer(
            f"Вы ввели сообщение: {decrypt_eng_answer}\nРезультат дешифровки: {decrypt}\nЕсли есть вопросы обратитесь к справке 🎮",
            reply_markup=nav.back_menu)

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()



# Переходим в меню Шифр Цезаря
@dp.message_handler(Text(equals="Шифр Цезаря"))
async def ciesar(message: types.Message):

    photo = InputFile(r'Caesar+cipher.jpg')

    await bot.send_photo(message.chat.id, photo=photo, caption="Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите.\n"
                                            "Например, в шифре со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее.\n"
                                            "Шифр назван в честь римского императора Гая Юлия Цезаря, использовавшего его для секретной переписки со своими генералами.\n\n❗ В этом боте сдвиг установлен вправо как самый часто используемый тип этого шифра ❗", reply_markup=nav.fourth_plane_menu_under_ciesar_ciphers)

# Шифр цезаря зашифровать / русский
@dp.message_handler(Text(equals="Шифр Цезаря: Зашифровать"), state=None)
async def ciesar_encrypt_en(message: types.Message):

    await bot.send_message(message.chat.id, "Выберите язык", reply_markup=nav.language_menu_to_ciesar_encrypto)

@dp.callback_query_handler(text="ciesar_encrypt_russain")
async def ciesar_rus_en_get_mes(call: types.CallbackQuery):

    await bot.answer_callback_query(call.id)

    await bot.send_message(call.from_user.id, "Введите сообщение на русском языке без знаков пунктуации", reply_markup=nav.baka_menu)

    await st.ciesar_encrypt.ciesar_encrypt_rus_mess.set()

    await call.answer()

@dp.message_handler(state=st.ciesar_encrypt.ciesar_encrypt_rus_mess)
async def ciesar_rus_get_shift(message: types.Message, state: FSMContext):
    try:

        async with state.proxy() as data:
            data['ciesar_message'] = str(message.text)

        data = await state.get_data()

        message_get = data.get("ciesar_message")

        if message_get == '/back':

            await bot.send_message(message.chat.id, "🏎 Перемещаемся в главное меню 🏎",
                                   reply_markup=nav.first_plane_menu)

        else :

            await bot.send_message(message.chat.id, "Введите число смещение\n(натуральное число не превышающее 32)", reply_markup=nav.baka_menu)

            await st.ciesar_encrypt.ciesar_encrypt_rus_shift_get.set()

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

@dp.message_handler(state=st.ciesar_encrypt.ciesar_encrypt_rus_shift_get)
async def find_load_shift(message: types.Message, state: FSMContext):

    try:
        async with state.proxy() as data:
            data['ciesar_shift_get'] = int(message.text)


    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

    try:

        data = await state.get_data()

        message_get = data.get("ciesar_message").upper()
        shift = data.get("ciesar_shift_get")

        int(shift)

        await state.finish()

        if (isinstance(shift, int)) and (shift >= 0) and (shift <= 32):

            alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

            alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

            caesar_reult_en_rus = ''

            for i in message_get:
                place = int(alfavit_RU.find(i))
                new_place = place + shift
                if i in alfavit_RU:
                    caesar_reult_en_rus += alfavit_RU[new_place]
                else:
                    caesar_reult_en_rus += i

            await bot.send_message(message.chat.id,
                                   f"Ваше сообщение: {message_get}\nРезультат шифрования: {caesar_reult_en_rus}\nКлюч шифрования: {shift}\nЕсли есть вопросы по работе шифра Цезаря, то обратитесь к справке 🎮",
                                   reply_markup=nav.baka_menu)

        else:

            await bot.send_message(message.chat.id,
                                   "Ошибка в заданом ключе!\nПараметр(ключ) - это целочисленное число, которое должено быть в заданом ограничении: 0 <= ключ <= 32\nПовторите попытку с валидным значением",
                                   reply_markup=nav.baka_menu)

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()


# Шифр цезаря зашифровать / англиский
@dp.callback_query_handler(text="ciesar_encrypt_english")
async def ciesar_rus_en_get_new(call: types.CallbackQuery):

    await bot.answer_callback_query(call.id)

    await bot.send_message(call.from_user.id, "Введите сообщение на англисском языке без знаков пунктуации", reply_markup=nav.baka_menu)

    await st.ciesar_encrypt.ciesar_encrypt_eng_mess.set()

    await call.answer()

@dp.message_handler(state=st.ciesar_encrypt.ciesar_encrypt_eng_mess)
async def ciesar_eng_en_get_mes(message: types.Message, state: FSMContext):
    try:

        async with state.proxy() as data:
            data['ciesar_message_english'] = str(message.text)

        data = await state.get_data()

        message_get = data.get("ciesar_message_english")

        if message_get == '/back':

            await bot.send_message(message.chat.id, "🏎 Перемещаемся в главное меню 🏎",
                                   reply_markup=nav.first_plane_menu)

        else :

            await bot.send_message(message.chat.id, "Введите число смещение\n(натуральное число не превышающее 25)", reply_markup=nav.baka_menu)

            await st.ciesar_encrypt.ciesar_encrypt_eng_shift.set()

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

@dp.message_handler(state=st.ciesar_encrypt.ciesar_encrypt_eng_shift)
async def find_load_shift_english(message: types.Message, state: FSMContext):

    try:
        async with state.proxy() as data:
            data['ciesar_shift_get_english'] = int(message.text)


    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

    try:

        data = await state.get_data()

        message_get = data.get("ciesar_message_english").upper()
        shift = data.get("ciesar_shift_get_english")

        await state.finish()

        caesar_reult_en_eng = ''

        if (isinstance(shift, int)) and (shift >= 0) and (shift <= 32):

            alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

            alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

            caesar_reult_en_rus = ''

            for i in message_get:
                place = int(alfavit_EU.find(i))
                new_place = place + shift
                if i in alfavit_EU:
                    caesar_reult_en_eng += alfavit_EU[new_place]
                else:
                    caesar_reult_en_eng += i

            await bot.send_message(message.chat.id, f"Ваше сообщение: {message_get}\nРезультат шифрования: {caesar_reult_en_eng}\n"
                                                    f"Ключ шифрования: {shift}\n"
                                                    f"Если есть вопросы по работе шифра Цезаря, "
                                                    f"то обратитесь к справке 🎮", reply_markup=nav.baka_menu)

        else:

           await bot.send_message(message.chat.id,
                                   "Ошибка в заданом ключе!\n"
                                   "Параметр(ключ) - это целочисленное число, которое должено быть в заданом ограничении: 0 <= ключ <= 32\nПовторите попытку с валидным значением",
                                   reply_markup=nav.back_menu)

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()


# Шифр цезаря расшифровать / русский
@dp.message_handler(Text(equals="Шифр Цезаря: Расшифровать"))
async def ciesar_decrypt_en(message: types.Message):

    await bot.send_message(message.chat.id, "Выберите язык", reply_markup=nav.language_menu_to_ciesar_decrypto)

@dp.callback_query_handler(text="ciesar_decrypt_russian")
async def ciesar_decrypt_russian_get(call: types.CallbackQuery):

    await bot.answer_callback_query(call.id)

    await bot.send_message(call.from_user.id, "Введите сообщение на русском языке без знаков пунктуации, которое нужно расшифровать", reply_markup=nav.baka_menu)

    await st.ciesar_decrypt.ciesar_decrypt_rus_mess.set()

    await call.answer()

@dp.message_handler(state=st.ciesar_decrypt.ciesar_decrypt_rus_mess)
async def ciesar_decrypt_english_getton(message: types.Message, state: FSMContext):

    try:

        async with state.proxy() as data:
            data['ciesar_decrypt_rus_message'] = str(message.text)

        data = await state.get_data()

        message_get = data.get("ciesar_decrypt_rus_message")

        if message_get == '/back':

            await bot.send_message(message.chat.id, "🏎 Перемещаемся в главное меню 🏎",
                                   reply_markup=nav.first_plane_menu)

        else:

            await bot.send_message(message.chat.id, "Введите число смещение\n(натуральное число не превышающее 32)", reply_markup=nav.baka_menu)


            await st.ciesar_decrypt.ciesar_decrypt_rus_shift_get.set()

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

@dp.message_handler(state=st.ciesar_decrypt.ciesar_decrypt_rus_shift_get)
async def ciesar_decrypt_russian_get_shift(message: types.Message, state: FSMContext):

    try:
        async with state.proxy() as data:
            data['ciesar_decrypt_get_rus'] = int(message.text)


    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

    alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    try:

        data = await state.get_data()

        message_get = data.get("ciesar_decrypt_rus_message").upper()
        shift = data.get("ciesar_decrypt_get_rus")

        caesar_reult_en_rus = ''

        await state.finish()

        if (isinstance(shift, int)) and (shift >= 0) and (shift <= 32):

            alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

            alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

            caesar_reult_en_rus = ''

            for i in message_get:
                place = int(alfavit_RU.find(i))
                new_place = place - shift
                if i in alfavit_RU:
                    caesar_reult_en_rus += alfavit_RU[new_place]
                else:
                    caesar_reult_en_rus += i

            await bot.send_message(message.chat.id,
                                   f"Ваше сообщение: {message_get}\nРезультат шифрования: {caesar_reult_en_rus}\nКлюч шифрования: {shift}\nЕсли есть вопросы по работе шифра Цезаря, то обратитесь к справке 🎮",
                                   reply_markup=nav.baka_menu)

        else:

            await bot.send_message(message.chat.id,
                                   "Ошибка в заданом ключе!\nПараметр(ключ) - это целочисленное число, которое должено быть в заданом ограничении: 0 <= ключ <= 32\nПовторите попытку с валидным значением",
                                   reply_markup=nav.baka_menu)

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()


# Шифр цезаря расшифровать / англиский
@dp.callback_query_handler(text="ciesar_decrypt_english")
async def ciesar_decrypt_english_get(call: types.CallbackQuery):

    await bot.send_message(call.from_user.id, "Введите сообщение на англиском языке без знаков пунктуации, которое нужно расшифровать", reply_markup=nav.baka_menu)

    await bot.answer_callback_query(call.id)

    await st.ciesar_decrypt.ciesar_decrypt_eng_mess.set()

    await call.answer()

@dp.message_handler(state=st.ciesar_decrypt.ciesar_decrypt_eng_mess)
async def ciesar_decrypt_english_getton(message: types.Message, state: FSMContext):

    try:

        async with state.proxy() as data:
            data['ciesar_decrypt_enlish'] = str(message.text)

        data = await state.get_data()

        message_get = data.get("ciesar_decrypt_rus_message")

        if message_get == '/back':

            await bot.send_message(message.chat.id, "🏎 Перемещаемся в главное меню 🏎",
                                   reply_markup=nav.first_plane_menu)

        else:

            await bot.send_message(message.chat.id, "Введите число смещение\n(натуральное число не превышающее 25)", reply_markup=nav.baka_menu)


            await st.ciesar_decrypt.ciesar_decrypt_eng_shift.set()

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

@dp.message_handler(state=st.ciesar_decrypt.ciesar_decrypt_eng_shift)
async def ciesar_decrypt_english_get_shift(message: types.Message, state: FSMContext):

    try:

        async with state.proxy() as data:
            data['ciesar_decrypt_enlish_shift'] = int(message.text)


    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

    try:

        alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

        alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

        data = await state.get_data()

        message_get = data.get("ciesar_decrypt_enlish").upper()
        shift = data.get("ciesar_decrypt_enlish_shift")

        caesar_reult_en_rus = ''

        if (isinstance(shift, int)) and (shift >= 0) and (shift <= 32):

            alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

            alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

            ciesar_decrypt_eng_send = ''

            for i in message_get:
                place = int(alfavit_EU.find(i))
                new_place = place - shift
                if i in alfavit_EU:
                    ciesar_decrypt_eng_send += alfavit_EU[new_place]
                else:
                    ciesar_decrypt_eng_send += i

            await bot.send_message(message.chat.id,
                                   f"Ваше сообщение: {message_get}\nРезультат шифрования: {ciesar_decrypt_eng_send}\nКлюч шифрования: {shift}\nЕсли есть вопросы по работе шифра Цезаря, то обратитесь к справке 🎮",
                                   reply_markup=nav.baka_menu)

        else:

            await bot.send_message(message.chat.id,
                               "Ошибка в заданом ключе!\nПараметр(ключ) - это целочисленное число, которое должено быть в заданом ограничении: 0 <= ключ <= 32\nПовторите попытку с валидным значением",
                               reply_markup=nav.baka_menu)

    except Exception as ex:

        await bot.send_message(message.chat.id, "Извините, вознили ошибки !", reply_markup=nav.back_menu)

        await state.finish()

# Возвращение в главное меню
@dp.message_handler(Text(equals="Назад"))
async def back(message: types.Message):

    await bot.send_message(message.chat.id, "🛸 Перемещаемся в главное меню 🛸", reply_markup=nav.first_plane_menu)


# О криптографии
@dp.message_handler(Text(equals="🔎 О криптографии 🔎"))
async def about_crypto(message: types.Message):

    await bot.send_message(message.chat.id, "Что тебя интересует ?\n", reply_markup=nav.about_crypto_menu)


# Команды
@dp.message_handler(Text(equals="📃 Список команд 📃"))
async def list_of_commands(message: types.Message):

    await bot.send_message(message.chat.id, "Список доступных команд:\n"
                                            "/start - Переход к главному меню\n"
                                            "/help - Помощь\n"
                                            "/rules - Правила пользования ботом\n"
                                            "/back - Возращение к начальной старнице в случае ошибки (нельзя использовать посередине выполнение шифровки и дешифровки)", reply_markup=nav.back_menu)


# Кол бэк на главное меню
@dp.callback_query_handler(text="back_to_main")
async def go_back(call: types.CallbackQuery):

    await bot.send_message(call.message.chat.id, "🏎 Перемещаемся в главное меню 🏎", reply_markup=nav.first_plane_menu)


# Правила
@dp.message_handler(Text(equals="Правила"))
async def rules_send_rules(message: types.Message):

    await bot.send_message(message.chat.id,"Правил тут немного:\n"
                                           "1 - Пользуйся кнопками, они тут не для красоты;\n"
                                           "2 - Читай все инструкции перед использованием алг. шифрования;\n"
                                           "3 - В случае отстутствия ответа от бота проверьте раскладку клавиатуры и повторите ввод;\n"
                                           "4 - Если не помогло перезапустите бота;\n\n"
                                           "На этом все, удачи ✌️", reply_markup=nav.second_info_menu)

@dp.message_handler(commands=['rules'])
async def rules(message: types.Message):

    await bot.send_message(message.chat.id,"Правил тут немного:\n"
                                           "1 - Пользуйся кнопками, они тут не для красоты;\n"
                                           "2 - Читай все инструкции перед использованием алг. шифрования;\n"
                                           "3 - В случае отстутствия ответа от бота проверьте раскладку клавиатуры и повторите ввод;\n"
                                           "4 - Если не помогло перезапустите бота;\n\n"
                                           "На этом все, удачи ✌️", reply_markup=nav.back_menu)



# Зачем это ?
@dp.message_handler(Text(equals="Зачем это ?"))
async def why_this(message: types.Message):

    await bot.send_message(message.chat.id, "Для этого бота можно найти много способов применения, но главным так это проверка того как вы справляетесь с"
                                            "заданиями на алгоритмы шифрования, а так же для продвижения в массы темы криптографии."
                                            " Этот сервис планируется развивать, а в раздел с информацией добавиться описание обновлений 😼", reply_markup=nav.trird_info_menu)



@dp.message_handler(Text(equals="Книги 📚"))
async def books(message: types.Message):

    await bot.send_message(message.chat.id, "Тут представлен список книг, которые по субъективному мнению автора "
                                            "могут помочь изучить и понимать криптографию и некоторые ее особенности\n")



    await bot.send_message(message.chat.id,
                                            "📚 - Код. Тайный язык информатики; Автор - Чарльз Петцольд\n"
                                            "📚 - Таинственные страницы; Автор - Иван Ефишов\n"
                                            "📚 - Прикладная криптография; Автор - Шнайер Брюс\n"
                                            "📚 - Грокаем алгоритмы; Автор - Бхаргава Адитья\n", reply_markup=nav.about_crypto_menu_first)



@dp.message_handler(Text(equals="Статьи 📝"))
async def articles(message: types.Message):

    await bot.send_message(message.chat.id, "Тут представлен список статей, которые по субъективному мнению автора "
                                            "помогут углубиться в особенности криптоанализа и даст больше практических навыков\n")





    await bot.send_message(message.chat.id, "Портал: Хабр - http://surl.li/bhzdk\n"
                                            "Портал: Хабр - http://surl.li/bhzdo\n"
                                            "Портал: ITNAN - http://surl.li/bhzdq\n"
                                            "Портал: TPROGER - http://surl.li/bhzdx\n", reply_markup=nav.about_crypto_menu_second)

@dp.message_handler(Text(equals="Видео 📹"))
async def send_videous(message: types.Message):


    await bot.send_message(message.chat.id, "Тут представлен ссылки на видеоресурсы, которые по субъективному мнению автора "
                                            "помогут углубиться в особенности криптоанализа и даст больше практических навыков")



    await bot.send_message(message.chat.id, "Канал: QWERTY - http://surl.li/bhzcd\n"
                                            "Канал: CryptoInside - http://surl.li/bhzcm\n"
                                            "Канал: Diana Dvoryak - http://surl.li/bhzcy\n", reply_markup=nav.about_crypto_menu_third)



@dp.message_handler(commands=['back'])
async def back(message: types.Message):


    await bot.send_message(message.chat.id, "🛸 Перемещаемся в главное меню 🛸", reply_markup=nav.first_plane_menu)





if __name__ == '__main__':
    try:

        print("...Бот запущен...")

        executor.start_polling(dp)

        print("...Бот выключен...")

    except Exception as ex:

        print(f"Возникли проблемы:\n{ex}")