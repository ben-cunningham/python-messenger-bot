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


## Usage 

### Basic Messages

Pybot's models represent Facebook Messenger API's JSON structure as closely as possible. We have made it as easy as possible to compose messages with templates, elements and buttons. 

A request to the Messenger API is composed of a recipient `id` and a `message`. Pybot's `Message` class corresponds to this. To construct a message, you must pass it the `type` and a `payload`. The most simple usage of the Messenger Platform is to respond with a text message, where the payload is the string, `'Hello, World'`:

```python
from fbmsgbot.bot import Bot
from fbmsgbot.models.message import Message

bot = Bot(<FACEBOOK_TOKEN>)

msg = Message('text', 'Hello, World!')
bot.send_message(msg, recipient_id)
```

#### Sending an Image Message
```python
msg = Message('image', 'http://www.myfiles.com/path/to/img.jpg')
bot.send_message(msg, recipient_id)
```

#### Sending an Audio Message
```python
msg = Message('audio', 'http://www.myfiles.com/path/to/audio.mp3')
bot.send_message(msg, recipient_id)
```

#### Sending a Video Message
```python
msg = Message('video', 'http://www.myfiles.com/path/to/video.mp4')
bot.send_message(msg, recipient_id)
```

#### Sending a File Message
```python
msg = Message('file', 'http://www.myfiles.com/path/to/pdf.pdf')
bot.send_message(msg, recipient_id)
```

### Structured Messages

The Messenger platform also allows users to send [structured messages](https://developers.facebook.com/docs/messenger-platform/send-api-reference/generic-template). These are composed of Templates which allow for rich media, buttons, and reciepts. 


#### Buttons

Buttons can either contain Web URLs or a payload for a postback. To construct them, you must pass `type`, `title`, and `payload`:
```python
from fbmsgbot.models.attachment import Button

web_button = Button(
    type='web_url',
    title='My title',
    payload='http://www.newton.ac.uk/files/covers/968361.jpg'
)
```

#### Generic Template
```python
from fbmsgbot.models.template import Template
from fbmsgbot.models.attachment import Button, Element

web_button = Button(
    type='web_url',
    title='My Button Image',
    payload='http://www.newton.ac.uk/files/covers/968361.jpg'
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

msg = Message('template', generic_template)
response, error = bot.send_message(msg2, recipient)
```

#### Button Template

```python
postback_button = Button(
    type='postback',
    title='My Postback',
    payload="<USER DEFINED PAYLOAD>",
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

```