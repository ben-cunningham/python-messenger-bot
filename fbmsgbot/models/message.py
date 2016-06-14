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

    def __init__(self, type):
        self.title = ''
        self.sub_title = ''
        self.buttons = []

    def to_json(self):
        return json.loads({})
