import logging
import os

from dotenv import load_dotenv

from bot.dispatcher import Dispatcher
from bot.handlers.echo import echo_handler
from bot.long_polling import start_long_polling
from bot.telegram_messenger import TelegramMessenger


def main() -> None:
    load_dotenv()

    token = os.environ["TELEGRAM_TOKEN"]
    base_url = os.environ["TELEGRAM_BASE_URL"]

    logging.basicConfig(level=logging.INFO)

    messenger = TelegramMessenger(token, base_url)

    dispatcher = Dispatcher(messenger)
    dispatcher.add_handler(echo_handler)

    print("Bot started. Waiting for messages...")

    start_long_polling(dispatcher, messenger)


if __name__ == "__main__":
    main()
