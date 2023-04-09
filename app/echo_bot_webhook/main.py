"""
This is a echo bot.
It echoes any incoming text messages.
"""


import os

import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook


load_dotenv("/run/secrets/echo_bot_webhook.env")

WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')

assert WEBHOOK_HOST, "WEBHOOK_HOST is None"
assert WEBHOOK_PATH, "WEBHOOK_PATH is None"

WEBHOOK_URL = f"{WEBHOOK_HOST}/{WEBHOOK_PATH}"

API_TOKEN = os.getenv('TELEGRAM_TOKEN')
assert API_TOKEN is not None, f"ECHO BOT WEBHOOK: telegram token is None."

# webserver settings
WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = os.getenv('WEBAPP_PORT')

assert WEBAPP_HOST, "WEBAPP_HOST is None"
assert WEBAPP_PORT, "WEBAPP_PORT is None"
# WEBAPP_HOST = '0.0.0.0'  # or ip
# WEBAPP_PORT = 9001

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler()

async def echo(message: types.Message):
    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    logging.warning(f'in_startup setting webhook address: {WEBHOOK_URL}')


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    logging.warning('Bye!')


if __name__ == '__main__':

    start_webhook(
        dispatcher=dp,
        webhook_path=f'/{WEBHOOK_PATH}',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
        ssl_context=None,
    )
