from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("Menyu 1"), KeyboardButton("Menyu 2"), KeyboardButton("Menyu 3"), KeyboardButton("Menyu 4")],
    [KeyboardButton("Menyu 5")],
        ],
    resize_keyboard=True)



# async def get_all_product():
menu_detail = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail.add(KeyboardButton("Mahsulot 1"), KeyboardButton("Mahsulot 2"))
menu_detail.add(KeyboardButton("Mahsulot 1"), KeyboardButton("Mahsulot 2"), KeyboardButton("Mahsulot 3"))
menu_detail.add(KeyboardButton("Back"))


