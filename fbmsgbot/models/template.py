from attachment import Button
import json 

class Template(object):
    """
    Facebook Messenger message
    model for structured messages
    """

    button_type = 'button'
    generic_type = 'generic'
    receipt_type = 'receipt'

    def __init__(self, type, **kwargs):
        self.type = type
        self.kwargs = kwargs

    def to_json(self):
        message = {}
        message['message'] = {
                'attachment' : {
                    'type' : 'template',
                }
            }

        if self.type == self.button_type:
            assert all([isinstance(button, Button)
            	for button in self.kwargs['buttons']]), "Missing type button"
            
            buttons = [json.loads(b.to_json()) for b in self.kwargs['buttons']]
            message['message']['attachment']['payload'] = {
                'template_type' : 'button',
                'text' : self.kwargs['title'],
                'buttons' : buttons
            }
        
        elif self.type == self.generic_type:
        	# elements = kwargs.get('elements')
        	# TODO: Check types and check if elements exist in kwargs
            elements = [json.loads(element.to_json()) for element in self.kwargs['elements']]
            message['message']['attachment']['payload'] = {
                'template_type' : 'generic',
                'elements': elements
            }
        
        elif self.type == self.receipt_type:
            raise NotImplementedError

        return payload
