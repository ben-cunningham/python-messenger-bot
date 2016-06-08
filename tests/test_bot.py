import unittest

import httpretty

from pybot.bot import Bot
from pybot.models.message import (
	TextMessage, 
	StructuredMessage
)
from pybot.resources.urls import FACEBOOK_MESSAGES_POST_URL

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

	def send_image_message(self):
		pass
