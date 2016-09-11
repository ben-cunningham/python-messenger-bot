

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
            buttons = [button.to_json() for button in self.buttons]

        payload = {
            'title': self.title,
            'image_url': self.image_url,
            'subtitle': self.subtitle,
            'buttons': buttons
        }

        return payload
