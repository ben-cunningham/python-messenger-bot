import unittest

import httpretty

from fbmsgbot.bot import Bot
from fbmsgbot.models.message import TextMessage
from fbmsgbot.models.message import StructuredMessage
from fbmsgbot.models.attachment import WebUrlButton
from fbmsgbot.models.attachment import Element
from fbmsgbot.resources.urls import FACEBOOK_MESSAGES_POST_URL

class TestBot(unittest.TestCase):

    def test_constructor(self):
        
        bot = Bot("abcdefg")
        assert bot.api_token == "abcdefg"
        assert bot.client is not None

    @httpretty.activate
    def test_send_text_message(self):

        httpretty.register_uri(httpretty.POST,
            FACEBOOK_MESSAGES_POST_URL + '/me/messages',
            body='{ \
                "recipient_id": 1008, \
                "message_id": "mid.1" \
            }', status=201)

        bot = Bot("abc")
        message = TextMessage(
                    "hello world!", 
                    "user_id")

        def completion(response):
            assert response['recipient_id'] == 1008
            assert response['message_id'] == "mid.1"

        bot.send_message(message, completion)

    def test_send_image_message(self):
        pass

    @httpretty.activate
    def test_send_button_structured_message(self):
        httpretty.register_uri(httpretty.POST,
            FACEBOOK_MESSAGES_POST_URL + '/me/messages',
            body='{ \
                "recipient_id": "1008", \
                "message_id": "mid.1" \
            }')

        bot = Bot("abc")
        buttons = []
        for i in range(3):
            buttons.append(WebUrlButton(str(i), "http://ex.com"))
        
        message = StructuredMessage(StructuredMessage.button_type)
        message.title = 'test title'
        message.buttons = buttons
        
        def completion(response):
            pass

        bot.send_message(message, completion)

    @httpretty.activate
    def test_send_generic_structured_message(self):
        httpretty.register_uri(httpretty.POST,
            FACEBOOK_MESSAGES_POST_URL + '/me/messages',
            body='{ \
                "recipient_id": "1008", \
                "message_id": "mid.1" \
            }')

    def test_single_messages_for_request(self):
        
        class TestObject(object):
            pass

        request = TestObject()
        request.json = {
            "entry": [
                {
                    "id": "721124344656842",
                    "messaging": [
                        {
                            "message": {
                                "mid": "mid.1466050624240:e96ba6183821bcf348",
                                "seq": 19,
                                "text": "test"
                            },
                            "recipient": {
                                "id": "721124344656842"
                            },
                            "sender": {
                                "id": "1428040060555694"
                            },
                            "timestamp": 1466050624267
                        },
                    ],
                    "time": 1466050648776
                }
            ],
            "object": "page"
        }

        bot = Bot("abc")
        messages = bot.messages_for_request(request)

        assert len(messages) == 1
        message = messages[0]
        assert message.type == 'text'
        assert message.text == 'test'

        


