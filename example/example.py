from flask import Flask
from flask import request

import sys
import os
sys.path.append("..")

from fbmsgbot.bot import Bot
from fbmsgbot.models.message import Message
from fbmsgbot.models.template import Template
from fbmsgbot.models.attachment import Button, Element, ReceiptElement 
import json

app = Flask(__name__)
bot = Bot(os.environ['PYBOT_TOKEN'])

def set_welcome():
    response, error = bot.set_welcome("Welcome to PyBot!")
    print response
    print error


@app.route('/', methods=['GET', 'POST'])
def webhook():
    # For webhook verification when registering app 
    if request.args.get("hub.verify_token") == 'test_token':
        return request.args.get("hub.challenge")

    # Recieve a list of available messages
    msgs = bot.messages_for_request(request)
    
    for m in msgs:
        text = m.text # Retrieve what user sent
        recipient = m.sender # Retrieve who sent it
         
        if text == 'template':

            web_button = Button(
                type='web_url',
                title='My Button Image',
                payload='http://www.newton.ac.uk/files/covers/968361.jpg'
            )

            postback_button = Button(
                type='postback',
                title='My Postback',
                payload="<USER DEFINED PAYLOAD>",
            )
            
            element = Element(
                title='Generic Template Element Title',
                subtitle='My subtitle',
                image_url='http://www.buffettworld.com/images/news_trump.jpg',
                buttons=[
                    web_button,
                ]
            )
            
            generic_template = Template(
                Template.generic_type,
                elements=[
                    element,                    
                ]
            )

            button_template = Template(
                Template.button_type,
                title='My Button template title',
                buttons=[
                    web_button, postback_button,
                ]
            )

            msg = Message('template', button_template)
            response, error = bot.send_message(msg, recipient)

            msg2 = Message('template', generic_template)
            response, error = bot.send_message(msg2, recipient)
        
        elif text == 'receipt':
            element = ReceiptElement(
                title='My Title',
                subtitle='A very good subtitle',
                quantity='15',
                price=1999,
                currency='CAD',
                image_url='http://www.newton.ac.uk/files/covers/968361.jpg'
            )

            receipt = Template(Template.receipt_type,
                recipient_name= 'A name',
                order_number='12345678902',
                currency='CAD',
                payment_method='Visa',
                order_url='http://petersapparel.com/order?order_id=123456',
                elements=[
                    element,
                ],
                address={
                    'street_1': '1 Hacker Way',
                    'city': 'Vancouver',
                    'state': 'BC',
                    'country': 'CA',
                    'postal_code': '1A1A1A'

                },
                summary={
                    'subtotal': 75.00,
                    'shipping_cost': 4.95,
                    'total_tax': 6.19,
                    'total_cost': 56.14
                }
            )

            msg = Message('template', receipt)
            response, error = bot.send_message(msg, recipient)

        else: 
            payload = text
            # Create image message
            msg = Message('image', 'http://www.buffettworld.com/images/news_trump.jpg')
            # Create audio message
            msg = Message('audio', 'http://www.stephaniequinn.com/Music/Canon.mp3')
            # Create video message
            msg = Message('video', 'http://clips.vorwaerts-gmbh.de/VfE_html5.mp4')
            # Create file message
            msg = Message('file', 'http://www.pdf995.com/samples/pdf.pdf' )
            
            # Echo back to user
            msg = Message('text', payload)
            # Send text message
            bot.send_message(msg, recipient)

    return 'OK'

if __name__ == "__main__":
    app.debug = True
    
    web_button = Button(
        type='web_url',
        title='My Button Image',
        payload='http://www.newton.ac.uk/files/covers/968361.jpg'
    )

    postback_button = Button(
        type='postback',
        title='My Postback',
        payload="My defined payload string",
    )
    
    bot.set_welcome("Welcome to PyBot!")
    bot.set_persistent_menu([
        web_button,
        postback_button,
    ])
    
    app.run(port=8000)
