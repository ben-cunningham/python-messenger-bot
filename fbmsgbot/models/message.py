import abc, json

class Message():
    __metaclass__  = abc.ABCMeta
 
    @abc.abstractmethod
    def to_json(self):
         """Returns json representation of message"""


class TextMessage(Message):
    """
    Facebook Messenger message
    model for simple text responses
    """

    def __init__(self, message, recipient):
        self.message = message
        self.recipient_id = recipient

    def to_json(self):
        message = {
            'message': self.message,
            'recipient': self.recipient_id
        }

        return json.dumps(message) 
    

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

