from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("Menyu"))


menu_detail_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail_keyboard.add(KeyboardButton("Product 1"), KeyboardButton("Product 2"))