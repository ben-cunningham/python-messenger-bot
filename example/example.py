from flask import Flask
from flask import request

import sys
import os
sys.path.append("..")

from fbmsgbot.bot import Bot
from fbmsgbot.models.message import Message
from fbmsgbot.models.template import Template
from fbmsgbot.models.attachment import WebUrlButton, Element

import json

app = Flask(__name__)
bot = Bot(os.environ['PYBOT_TOKEN'])

def set_welcome():
	response, error = bot.set_welcome("Welcome to PyBot!")
	print response
	print error


@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.args.get("hub.verify_token") == 'test_token':
        return request.args.get("hub.challenge")

    msgs = bot.messages_for_request(request)
    for m in msgs:

    	msg = None

    	if not hasattr(m, 'text'):
    		break

    	if m.text == 'button':
    		buttons = []
    		b = WebUrlButton('google', 'https://www.google.ca')
    		buttons.append(b)
    		elements = [Element('test', 'http://www.newton.ac.uk/files/covers/968361.jpg', 'test subtitle', buttons)]
    		tmpl = Template('generic', elements=elements)

    		payload = tmpl
    		msg = Message(m.sender, 'template', payload)
    	else:
    		payload = m.text
    		msg = Message(m.sender, 'text', payload)

    	response, error = bot.send_message(msg)

    	if error:
    		return 'Bad Request'

    return 'OK'

if __name__ == "__main__":
	app.debug = True
	set_welcome()
	app.run(port=8000)
