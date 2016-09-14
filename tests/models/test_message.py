import unittest, json

from fbmsgbot.models.message import Message
from fbmsgbot.models.template import Template
from fbmsgbot.models.attachment import Button, Element, ReceiptElement

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

    def test_receipt_template(self):
        element = ReceiptElement(
            title='My Title',
            subtitle='A very good subtitle',
            quantity='15',
            price=1999,
            currency='CAD',
            image_url='google.com'
        )
        """
        @TODO:
        USED FOR TESTING FAILURE AND RAISING EXCEPTIONS
        # element2 = ReceiptElement(
        #     title='My Title',
        #     subtitle='A very good subtitle',
        #     image_url='google.com'
        # )
        """
        receipt = Template(Template.receipt_type,
            recipient_name= 'name',
            order_number='1',
            currency='CAD',
            payment_method='Visa',
            order_url='google.com',
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

        receipt = receipt.to_json()
        assert receipt['recipient_name'] == 'name'
        assert receipt['order_number'] == '1'
        assert receipt['currency'] == 'CAD'
        assert receipt['payment_method'] == 'Visa'
        assert receipt['order_url'] == 'google.com'

