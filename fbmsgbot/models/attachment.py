import json

"""
@brief: facebook message button super class
"""
class Button(object):
    
    def __init__(self, type_, title, payload):
        self.title = title
        self.type = type_
        self.payload = payload

    def to_json(self):
        request_payload = {}
        
        if self.type == 'web_url':
            request_payload['url'] = self.payload
        
        if self.type == 'postback':
            request_payload['payload'] = self.payload

        request_payload['title'] = self.title
        request_payload['type'] = self.type

        return request_payload

"""
@brief: elements live inside of structured messages 
"""
class Element():

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
