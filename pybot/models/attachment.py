import json

class Button():
    """
    Button object
    """

    def __init__(self, type, title, payload):
        self.title = title
        self.type = type
        if self.type == 'web_url':
            self.url = payload
        elif self.type == 'postback':
            self.payload = payload
        else:
            raise

    def to_json(self):
        
        payload = {
            'title': self.title,
            'type': self.type,
        }

        if self.url is not None:
            payload['url'] = self.url
        else:
            payload['payload'] = self.payload

        return json.dumps(payload)


class Element():
    """
    Element object
    """

    def __init__(self, title, image_url, subtitle, buttons):
        self.title = title
        self.image_url = image_url
        self.subtitle = subtitle

        if len(buttons) == 0:
            self.buttons = []
        else:
            self.buttons = buttons

    def to_json(self):

        buttons = []
        
        for button in self.buttons:
            buttons.append(button.to_json)

        payload = {
            'title': self.title,
            'image_url': self.image_url,
            'subtitle': self.subtitle,
            'buttons': button
        }

        return json.dumps(payload)

