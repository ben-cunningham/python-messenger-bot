import json

"""
@brief: facebook message button super class
"""
class Button(object):
    
    def __init__(self, type_, title):
        self.title = title
        self.type = type_

    def to_json(self):
        request_payload = {}
        
        if self.type == 'web_url':
            request_payload['url'] = self.url
        if self.type == 'postback':
            request_payload['payload'] = self.payload

        request_payload['title'] = self.title
        request_payload['type'] = self.type

        return json.dumps(request_payload)

class PayloadButton(Button):

    def __init__(self, title, payload):
        super(PayloadButton, self).__init__('postback', title)  
        self.payload = payload

class WebUrlButton(Button):
    
    def __init__(self, title, url):    
        super(WebUrlButton, self) .__init__('web_url', title)
        self.url = url


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

        return json.dumps(payload)

