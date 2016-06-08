import unittest, json

from pybot.models.message import TextMessage

class TestMessage(unittest.TestCase):
    """
    Test the Message models
    """

    def test_text_message(self):
        message = TextMessage('test message', '123abc')
        assert message.message == 'test message'
        assert message.recipient_id == '123abc'

    def test_text_message_to_json(self):
        message = TextMessage('test message', '123abc')
        json_ = message.to_json()
        json_ = json.loads(json_)
        assert json_['message'] == 'test message'
        assert json_['recipient'] == '123abc'
