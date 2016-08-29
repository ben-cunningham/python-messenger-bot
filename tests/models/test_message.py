import unittest, json

from fbmsgbot.models.message import Message
from fbmsgbot.models.template import Template
from fbmsgbot.models.attachment import Button
from fbmsgbot.models.attachment import Element


class TestMessage(unittest.TestCase):
    """
    Test the Message models
    """

    def test_message(self):
        message = Message('image', 'google.com')
        assert message.type == 'image'
        assert message.payload == 'google.com'

    def test_text_message_to_json(self):
        message = Message('image', 'google.com')
        json_ = message.to_json()
        print json_
        assert json_['attachment']['type'] == 'image'
        assert json_['attachment']['payload']['url'] == 'google.com'


class TestTemplate(unittest.TestCase):
    """
    Test the structuredMessage model
    """

    def test_button_template_button(self):
        buttons = [Button('web_url', 'title', 'url') for _ in range(3)]
        message = Template(
                        Template.button_type,
                        buttons=buttons,
                        title='title',
                  )

        payload = message.to_json()
        assert payload['template_type'] == 'button'
        assert payload['text'] == 'title'
        assert payload['buttons'][0]['title'] =='title'

        assert len(payload['buttons']) == 3

    def test_generic_template(self):
        title = 't'
        img_url = 'www.e.com'
        subtitle = 's'
        buttons = [Button('web_url', 'title', 'url') for i in range(3)]
        largs = [title, img_url, subtitle, buttons]
        elements = [Element(title,
                            img_url,
                            subtitle,
                            buttons)]


        message = Template(Template.generic_type,
                        elements=elements,)

        payload = message.to_json()
        assert payload['template_type'] == 'generic'
        assert payload['elements'][0]['title'] =='t'
