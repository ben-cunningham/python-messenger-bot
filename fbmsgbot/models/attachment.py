

class Button(object):
    """Button object, used for creating button messages"""

    def __init__(self, type=None, title="", payload=""):
        # Type: request param key
        valid_types = {
            'web_url': 'url',
            'postback': 'payload'
        }

        assert type in valid_types, "Type %s is not a Button type" \
            % (type,)

        self.title = title
        self.type = type
        self.typekey = valid_types[type]
        self.payload = payload

    def to_json(self):

        request_payload = {}
        request_payload[self.typekey] = self.payload
        request_payload['title'] = self.title
        request_payload['type'] = self.type

        return request_payload


class Element(object):
    """Elements are features of Templates"""

    def __init__(self, title="", subtitle="", image_url="", buttons=None):

        self.title = title
        self.image_url = image_url
        self.subtitle = subtitle
        self.buttons = buttons

    def to_json(self):

        if self.buttons:
            if not all(isinstance(button, Button) 
                for button in self.buttons):
                    raise TypeError("Buttons list contained non-type Button")

            buttons = [button.to_json() for button in self.buttons]
        
        payload = {
            'title': self.title,
            'image_url': self.image_url,
            'subtitle': self.subtitle,
            'buttons': buttons
        }

        return payload

class ReceiptElement(Element):

    def __init__(self, quantity=None, price=None, 
                       currency="CAD", **kwargs):

        self.kwargs = kwargs
        super(ReceiptElement, self).__init__(**self.kwargs)
        
        if price is None:
            raise ValueError("Incorrect keyword-argument given for type ReceiptElement, needed: price") 
        
        self.quantity = quantity
        self.price = price
        self.currency = currency


    def to_json(self):

        payload = {
            'title': self.title,
            'subtitle': self.subtitle,
            'quantity': self.quantity,
            'price': self.price,
            'currency': self.currency,
            'image_url': self.image_url
        }

        return payload
