import unittest
from unittest.mock import Mock

from bot.dispatcher import Dispatcher
from bot.messenger import Messenger


class TestDispatcher(unittest.TestCase):
    def setUp(self) -> None:
        self.messenger = Mock(spec=Messenger)
        self.dispatcher = Dispatcher(self.messenger)
        self.handler = Mock()

        self.dispatcher.add_handler(self.handler)

    def test_text_message(self) -> None:
        message = {
            "chat": {"id": 123},
            "text": "Привет",
        }
        update = {"update_id": 1, "message": message}

        self.dispatcher.dispatch(update)

        self.handler.assert_called_once_with(message, self.messenger)

    def test_update_without_message(self) -> None:
        update = {"update_id": 2}

        self.dispatcher.dispatch(update)

        self.handler.assert_not_called()

    def test_empty_message(self) -> None:
        update = {"update_id": 3, "message": None}

        self.dispatcher.dispatch(update)

        self.handler.assert_not_called()


if __name__ == "__main__":
    unittest.main()
