from aiogram.dispatcher.filters.state import StatesGroup, State



class get_language(StatesGroup):
    what_language_revers_encrypt = State()
    what_language_revers_decrypt = State()
    think_encr = State()
    think_decr = State()

class reverse_cipher_encrypt(StatesGroup):
    reverse_cipher_encrypt_english = State()
    reverse_cipher_encrypt_russian = State()

class reverse_cipher_dectypt(StatesGroup):
    reverse_cipher_dectypt_english = State()
    reverse_cipher_dectypt_russian = State()

class ciesar_encrypt(StatesGroup):
    ciesar_encrypt_rus_mess = State()
    ciesar_encrypt_rus_shift = State()
    ciesar_encrypt_rus_shift_get = State()
    ciesar_encrypt_eng_mess = State()
    ciesar_encrypt_eng_shift = State()

class ciesar_decrypt(StatesGroup):
    ciesar_decrypt_rus_mess = State()
    ciesar_decrypt_rus_shift = State()
    ciesar_decrypt_rus_shift_get = State()
    ciesar_decrypt_eng_mess = State()
    ciesar_decrypt_eng_shift = State()

class vizhers_encypt(StatesGroup):
    ciesar_encrypt_eng_mess = State()
    ciesar_encrypt_eng_shift = State()
    ciesar_encrypt_eng_shift_get = State()

class vizhers_decrypt(StatesGroup):
    ciesar_decrypt_eng_mess = State()
    ciesar_decrypt_eng_shift = State()
    ciesar_decrypt_eng_shift_get = State()

class send_to_friend(StatesGroup):

    # Обрантый шифр

    rev_en_ru = State()
    rev_en_en = State()
    rev_de_ru = State()
    rev_de_en = State()

    # Шифр Цезаря

    ciesar_en_ru = State()
    ciesar_en_en = State()
    ciesar_de_ru = State()
    ciesar_de_en = State()
