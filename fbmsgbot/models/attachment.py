import json


class Button(object):
    """Button object"""
    
    def __init__(self, type_, title, payload):
        # Type: request param key 
        valid_types = {
            'web_url': 'url',
            'postback': 'payload'
        }

        assert type_ in valid_types, "Type %s is not a Button type" \
            % (type_,)
        
        self.title = title
        self.type = type_
        self.typekey = valid_types[type_]
        self.payload = payload


    def to_json(self):
        request_payload = {}

        request_payload[self.typekey] = self.payload
        request_payload['title'] = self.title
        request_payload['type'] = self.type

        return request_payload


class Element():
    """Elements are features of Templates""" 

    def __init__(self, title, image_url, subtitle, buttons):
        
        self.title = title
        self.image_url = image_url
        self.subtitle = subtitle

        assert type(buttons) == type([])
        self.buttons = buttons

    def to_json(self):

        buttons = [button.to_json() for button in self.buttons]

        payload = {
            'title': self.title,
            'image_url': self.image_url,
            'subtitle': self.subtitle,
            'buttons': buttons
        }

        return payload
