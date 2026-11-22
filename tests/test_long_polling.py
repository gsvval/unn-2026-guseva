import unittest
from unittest.mock import Mock

from bot.dispatcher import Dispatcher
from bot.long_polling import poll_once
from bot.messenger import Messenger


class TestLongPolling(unittest.TestCase):
    def setUp(self) -> None:
        self.messenger = Mock(spec=Messenger)
        self.dispatcher = Mock(spec=Dispatcher)

    def test_no_updates(self) -> None:
        self.messenger.get_updates.return_value = []

        offset = poll_once(self.dispatcher, self.messenger, 0)

        self.assertEqual(offset, 0)
        self.dispatcher.dispatch.assert_not_called()

    def test_one_update(self) -> None:
        update = {
            "update_id": 10,
            "message": {"chat": {"id": 123}, "text": "Привет"},
        }
        self.messenger.get_updates.return_value = [update]

        offset = poll_once(self.dispatcher, self.messenger, 0)

        self.assertEqual(offset, 11)
        self.dispatcher.dispatch.assert_called_once_with(update)

    def test_multiple_updates(self) -> None:
        updates = [
            {"update_id": 10, "message": {"text": "Первое"}},
            {"update_id": 11, "message": {"text": "Второе"}},
        ]
        self.messenger.get_updates.return_value = updates

        offset = poll_once(self.dispatcher, self.messenger, 0)

        self.assertEqual(offset, 12)
        self.assertEqual(self.dispatcher.dispatch.call_count, 2)

    def test_polling_parameters(self) -> None:
        self.messenger.get_updates.return_value = []

        poll_once(self.dispatcher, self.messenger, 5)

        self.messenger.get_updates.assert_called_once_with(
            offset=5,
            limit=10,
            timeout=30,
            allowed_updates=["message"],
        )


if __name__ == "__main__":
    unittest.main()
