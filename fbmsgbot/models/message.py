
supported_types = [
    'text',
    'image',
    'video',
    'audio',
    'file',
    'template',
    'quick',
]


class Message():
    """
    Base message object
    """

    def __init__(self, type, payload, **kwargs):

        assert type in supported_types, 'That is not a supported type'

        self.type = type
        self.payload = payload
        self.kwargs = kwargs
   
    def to_json(self):
        """Returns json representation of message"""
        data = {}

        if self.type == 'text':
            data['text'] = self.payload

        elif self.type == 'quick':
            data['text'] = self.payload
            data['quick_replies'] = [reply.to_json() for reply in self.kwargs['quick_replies']]

        elif self.type in supported_types: # Attachment msg

            data['attachment'] = {}
            data['attachment']['type'] = self.type
            if self.type == 'template':
                template = self.payload
                data['attachment']['payload'] = template.to_json()
            
            else: # Images, audio, video etc
                data['attachment']['payload'] = {
                    'url': self.payload
                }
            
        else:
            raise TypeError("Type provided is not in supported types.")

        return data


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


class QuickReply():
    allowed = ['text', 'location']
    def __init__(self, type, title=None, payload=None, url=""):
        self.type = type
        if self.type not in self.allowed:
            raise ValueError("Specified type %s is not in allowed typed."
                % (self.type,) 
            )

        if self.type == 'text':
            if title is None or payload is None:
                raise ValueError("Text quickreplies must have a title and payload.")
            self.title = title
            self.payload = payload

        self.url = url

    def to_json(self):

        data = {}
        data['content_type'] = self.type

        if self.type == 'text':
            data['title'] = self.title
            data['payload'] = self.payload

        if self.url:
            data['image_url'] = self.url

        return data 

