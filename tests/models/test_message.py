import unittest, json

from fbmsgbot.models.message import TextMessage
from fbmsgbot.models.message import StructuredMessage

from fbmsgbot.models.attachment import WebUrlButton

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


class TestStructuredMessage(unittest.TestCase):
    """
    Test the structuredMessage model
    """

    def test_button_structured_button(self):
        message = StructuredMessage(StructuredMessage.button_type)
        message.title = 'title'
        message.buttons = [WebUrlButton('title', 'url') for i in range(3)]
        json_ = message.to_json()
        json_ = json.loads(json_)
        assert json_['message']['attachment']['type'] == 'template'

        payload = json_['message']['attachment']['payload']
        assert payload['template_type'] == 'button'
        assert payload['text'] == 'title'
        assert len(payload['buttons']) == 3


