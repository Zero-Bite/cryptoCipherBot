from aiogram import types

# Кнопки (клавиатура)
first_plane_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
second_plane_menu_ciphers = types.ReplyKeyboardMarkup(resize_keyboard=True)
thrird_plane_menu_under_reverse_ciphers = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
fourth_plane_menu_under_ciesar_ciphers = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
fifth_plane_menu_under_vizher_ciphers = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
info_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
second_info_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
trird_info_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
about_crypto_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
about_crypto_menu_first = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
about_crypto_menu_second = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
about_crypto_menu_third = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
back_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
baka_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
send_friend = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# Кнопки (инлайн режима)
language_menu = types.InlineKeyboardMarkup(row_width=2)
language_menu_to_ciesar_encrypto = types.InlineKeyboardMarkup(row_width=2)
language_menu_to_ciesar_decrypto = types.InlineKeyboardMarkup(row_width=2)
language_vizher_menu = types.InlineKeyboardMarkup(row_width=1)
language_vizher_menu_decrypt = types.InlineKeyboardMarkup(row_width=1)

# кнопки главного меню

item_1 = types.KeyboardButton("ℹ️ InFo ℹ️")
item_2 = types.KeyboardButton("🔐 Шифры 🔐")
item_3 = types.KeyboardButton("🔎 О криптографии 🔎")
item_4 = types.KeyboardButton("📃 Список команд 📃")

# кнопки меню шифров

reverse_ciphers = types.KeyboardButton("Шифр Вижера")
ciesar_ciphers = types.KeyboardButton("Шифр Цезаря")
vizher_ciphers = types.KeyboardButton("Шифр Атбаша")
back = types.KeyboardButton("Назад")

# кноки выбора действий в шифрах

# Шифр Вижера
reverse_ciphers_encrypt = types.KeyboardButton("Шифр Вижера: Зашифровать")
reverse_ciphers_decrypt = types.KeyboardButton("Шифр Вижера: Расшифровать")
revers_sients = types.KeyboardButton("Подробнее об ученом 👨‍🏫")
reverse_ciphers_encrypt_inline = types.InlineKeyboardButton(text="Англиский", callback_data="reverse_ciphers_encrypt_inline_en")
reverse_ciphers_decrypt_inline = types.InlineKeyboardButton(text="Англиский", callback_data="reverse_ciphers_decrypt_inline")

# Шифр Цезаря
ciesar_ciphers_ecrypt = types.KeyboardButton("Шифр Цезаря: Зашифровать")
ciesar_encrypt_russain = types.InlineKeyboardButton(text="Русский", callback_data="ciesar_encrypt_russain")
ciesar_encrypt_english = types.InlineKeyboardButton(text="Англиский", callback_data="ciesar_encrypt_english")

ciesar_ciphers_decrypt = types.KeyboardButton("Шифр Цезаря: Расшифровать")
ciesar_decrypt_russian = types.InlineKeyboardButton(text="Русский", callback_data="ciesar_decrypt_russian")
ciesar_decrypt_english = types.InlineKeyboardButton(text="Англиский", callback_data="ciesar_decrypt_english")

# Обратный шифр
vizher_ciphers_encrypt = types.KeyboardButton("Шифр Атбаша: Зашифровать")
vizher_ciphers_decrypt = types.KeyboardButton("Шифр Атбаша: Расшифровать")

# Выбор языка для обратного шифро
english_revers_encrypt = types.InlineKeyboardButton(text="Англисский", callback_data="english_revers_encrypt")
russian_revers_encrypt = types.InlineKeyboardButton(text="Русский", callback_data="russian_revers_encrypt")
back_to_main = types.InlineKeyboardButton(text = "Назад", callback_data="back_to_main")
english_revers_decrypt = types.InlineKeyboardButton(text="Англисский", callback_data="english_revers_decrypt")
russian_revers_decrypt = types.InlineKeyboardButton(text ="Русский", callback_data="russian_revers_decrypt")

# Информация
info_item_1 = types.KeyboardButton("Зачем это ?")
info_item_2 = types.KeyboardButton("Правила")

# О криптографии

about_crypto_books = types.KeyboardButton("Книги 📚")
about_crypto_sites = types.KeyboardButton("Статьи 📝")
about_crypto_videos = types.KeyboardButton("Видео 📹")


# Экстренный возврат в главное меню

baka = types.KeyboardButton("/back")

# подключение кнопок к меню
first_plane_menu.add(item_1, item_2, item_3, item_4)
second_plane_menu_ciphers.add(reverse_ciphers, ciesar_ciphers, vizher_ciphers ,back)
thrird_plane_menu_under_reverse_ciphers.add(reverse_ciphers_encrypt, reverse_ciphers_decrypt, revers_sients,back)
fourth_plane_menu_under_ciesar_ciphers.add(ciesar_ciphers_ecrypt, ciesar_ciphers_decrypt, back)
fifth_plane_menu_under_vizher_ciphers.add(vizher_ciphers_encrypt, vizher_ciphers_decrypt, back)
language_menu.add(english_revers_encrypt, russian_revers_encrypt, back_to_main)
language_menu_to_ciesar_encrypto.add(ciesar_encrypt_english,ciesar_encrypt_russain, back_to_main)
language_menu_to_ciesar_decrypto.add(ciesar_decrypt_english,ciesar_decrypt_russian, back_to_main)
language_vizher_menu.add(reverse_ciphers_encrypt_inline, back_to_main)
language_vizher_menu_decrypt.add(reverse_ciphers_decrypt_inline, back_to_main)
info_menu.add(info_item_1, info_item_2, back)
second_info_menu.add(info_item_1, back)
trird_info_menu.add(info_item_2, back)
about_crypto_menu.add(about_crypto_books, about_crypto_sites, about_crypto_videos, back)
about_crypto_menu_first.add(about_crypto_sites, about_crypto_videos, back)
about_crypto_menu_second.add(about_crypto_books, about_crypto_videos, back)
about_crypto_menu_third.add(about_crypto_books, about_crypto_sites, back)
back_menu.add(back)
baka_menu.add(baka)