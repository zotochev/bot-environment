"""
This is a echo bot.
It echoes any incoming text messages.
"""


import os

import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


load_dotenv("/run/secrets/echo_bot_webhook.env")

WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')

assert WEBHOOK_HOST, "WEBHOOK_HOST is None"
assert WEBHOOK_PATH, "WEBHOOK_PATH is None"

WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"


API_TOKEN = os.getenv('TELEGRAM_TOKEN')
assert API_TOKEN is not None, f"ECHO BOT: telegram token is None."

# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
