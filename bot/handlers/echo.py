from typing import Any

from bot.messenger import Messenger


def echo_handler(message: dict[str, Any], messenger: Messenger) -> None:
    text = message.get("text")

    if not isinstance(text, str):
        return

    chat = message.get("chat")
    if not isinstance(chat, dict):
        return

    chat_id = chat.get("id")
    if not isinstance(chat_id, int):
        return

    messenger.send_message(chat_id=chat_id, text=text)
