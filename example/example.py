from flask import Flask
from flask import request

import sys
import os
sys.path.append("..")

from fbmsgbot.bot import Bot
from fbmsgbot.models.message import Message

import json

app = Flask(__name__)
bot = Bot(os.environ['PYBOT_TOKEN'])

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.args.get("hub.verify_token") == 'test_token':
        return request.args.get("hub.challenge")

    msgs = bot.messages_for_request(request)
    for m in msgs:
    	msg = Message(m.sender, 'text', m.text)
    	response, error = bot.send_message(msg)

    	if error:
    		return 'Bad Request'

    return 'OK'

if __name__ == "__main__":
    app.run(port=8000)