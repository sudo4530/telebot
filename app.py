import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from default_button import menu_keyboard

API_TOKEN = "7450181024:AAHK4U9bJ5Pcbib3GoluxgHdo2uu87ieL08"


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    ful_name = message.from_user.full_name
    await message.reply(f"Assalomu aleykum sizni ko'rganimdan xursantman  {ful_name}", reply_markup=menu_keyboard)


@dp.message_handler(commands=['info'])
async def command_botinfo(message: types.Message):
    await message.reply("information ", reply_markup=ReplyKeyboardMarkup([
        [KeyboardButton("Share a number", request_contact=True)]
    ], resize_keyboard=True, one_time_keyboard=True))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
