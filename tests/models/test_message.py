import unittest, json

from fbmsgbot.models.message import Message
from fbmsgbot.models.message import StructuredMessage

from fbmsgbot.models.attachment import WebUrlButton

class TestMessage(unittest.TestCase):
    """
    Test the Message models
    """

    def test_message(self):
        message = Message('123abc', 'image', 'google.com')
        assert message.type == 'image'
        assert message.payload == 'google.com'
        assert message.recipient == '123abc'

    def test_text_message_to_json(self):
        message = Message('123abc', 'image', 'google.com')
        json_ = message.to_json()
        json_ = json.loads(json_)
        assert json_['attachment']['type'] == 'image'
        assert json_['attachment']['payload']['url'] == 'google.com'


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


