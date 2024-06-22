import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from default_button import menu_keyboard, menu_detail_keyboard
from inline_button import product_menu
from dotenv import load_dotenv
load_dotenv()


API_TOKEN = os.getenv("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    await message.reply(f"Salom @{username}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Menyu")
async def menyu(message: types.Message):
    await message.reply("Mahsulotlardan birini tanglang", reply_markup=menu_detail_keyboard)

@dp.message_handler(lambda message: message.text == "Product 1")
async def menyu_inline(message: types.Message):
    await message.reply("Mahsulot", reply_markup=product_menu)

@dp.message_handler(lambda message: message.text == "Back")
async def back(message: types.Message):
    await message.reply("Menyu", reply_markup=menu_keyboard)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)