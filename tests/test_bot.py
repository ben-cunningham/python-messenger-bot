import unittest

import httpretty

from fbmsgbot.bot import Bot
from fbmsgbot.models.message import TextMessage
from fbmsgbot.models.message import StructuredMessage
from fbmsgbot.models.attachment import Button
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
                "recipient_id": "1008", \
  				"message_id": "mid.1" \
            }')

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
	def test_send_button_structured_message():
		httpretty.register_uri(httpretty.POST,
            FACEBOOK_MESSAGES_POST_URL + '/me/messages',
            body='{ \
                "recipient_id": "1008", \
  				"message_id": "mid.1" \
            }')

		bot = Bot("abc")
		buttons = []
		for i in range(3):
			buttons.append(Button('web_url', i, "http://ex.com"))
		
		message = StructuredMessage("example", "ex_subtitle", buttons)
		
		def completion(response):
			pass

		bot.send_message(message, completion)

	def test_send_generic_structured_message():
		pass

