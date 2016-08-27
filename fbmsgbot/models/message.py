import json

class Message():
    """
    Base message object
    """

    def __init__(self, recipient, type, **kwargs):

        self.recipient = recipient
        self.type = type
        self.kwargs = kwargs

    def to_json(self, text=None, attachment=None):
         """Returns json representation of message"""

        data = {}

        if self.type == 'text':
            data['text'] = self.kwargs['text']
        else:
            data['attachment'] = {}
            data['attachment']['type'] = self.type
            elif self.type == 'template':
                template = self.kwargs['template']
                data['attachment']['payload'] = template.to_json()
            else:
                data['attachment']['payload']['url'] = self.kwargs['url']
    
class StructuredMessage(Message):
    """
    Facebook Messenger message
    model for structured messages
    """

    button_type = 'button'
    generic_type = 'generic'

    def __init__(self, type):
        self.title = ''
        self.sub_title = ''
        self.buttons = []
        self.type = type

    def to_json(self):
        message = {}
        message['message'] = {
                'attachment' : {
                    'type' : 'template',
                }
            }

        if self.type == self.button_type:
            message['message']['attachment']['payload'] = {
                'template_type' : 'button',
                'text' : self.title,
                'buttons' : [b.to_json() for b in self.buttons]
            }
        else:
            pass

        return json.dumps(message)

class ReceivedMessage(Message):
    """
    Model to represent reciepts
    """

    def __init__(self, json):

        if 'text' in json['message']:
            self.type = 'text'
            self.text = json['message']['text']

        self.recipient = json['recipient']['id']
        self.sender = json['sender']['id']
        self.time = json['timestamp']

    def to_json(self):
        raise NotImplementedError

