import unittest
from unittest.mock import Mock

from bot.handlers.echo import echo_handler
from bot.messenger import Messenger


class TestEchoHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.messenger = Mock(spec=Messenger)

    def test_text_message(self) -> None:
        message = {
            "chat": {"id": 123},
            "text": "Привет",
        }

        echo_handler(message, self.messenger)

        self.messenger.send_message.assert_called_once_with(
            chat_id=123,
            text="Привет",
        )

    def test_sticker_message(self) -> None:
        message = {
            "chat": {"id": 123},
            "sticker": {"file_id": "12345"},
        }

        echo_handler(message, self.messenger)

        self.messenger.send_message.assert_not_called()

    def test_message_without_chat(self) -> None:
        message = {"text": "Привет"}

        echo_handler(message, self.messenger)

        self.messenger.send_message.assert_not_called()


if __name__ == "__main__":
    unittest.main()
