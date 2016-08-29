# pybot
Python library for Facebook Messenger bot API

## To install

`pip install -r requirements.txt`

## To run test suites

`nosetests tests`

## Before submitting

You should run `flake8 <PATH_TO_CODE>` to ensure changes conform to PEP8 standards

## To Submit a new build to pip

1. Add a new tag to repo 
	`git tag -a <TAG> -m "<MESSAGE>"`
2. Push the new tag
	`git push origin --tags`
3. Update the `setup.py` file 
	* Update version to latest tag
	* Update the download url for latest tag
4. Upload to pip
	`python setup.py sdist upload`


## Quick Usage 

```python
from fbmsgbot.bot import Bot
from fbmsgbot.models.message import Message
from fbmsgbot.models.template import Template
from fbmsgbot.models.attachment import Button, Element

bot = Bot(<USER'S_FACEBOOK_TOKEN>)

# Send regular 'text' message
payload = "My message"
msg = Message('text', payload)
bot.send_message(msg, recipient)

# Send Template Messages
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
    title="My Button template title",
    buttons=[
        web_button, postback_button
    ]
)

msg = Message('template', button_template)
response, error = bot.send_message(msg, recipient)

msg2 = Message('template', generic_template)
response, error = bot.send_message(msg2, recipient)


```