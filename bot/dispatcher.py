from collections.abc import Callable
from typing import Any

from bot.messenger import Messenger

MessageHandler = Callable[[dict[str, Any], Messenger], None]


class Dispatcher:
    def __init__(self, messenger: Messenger) -> None:
        self.messenger = messenger
        self.handlers: list[MessageHandler] = []

    def add_handler(self, handler: MessageHandler) -> None:
        self.handlers.append(handler)

    def dispatch(self, update: dict[str, Any]) -> None:
        message = update.get("message")

        if not isinstance(message, dict):
            return

        for handler in self.handlers:
            handler(message, self.messenger)
