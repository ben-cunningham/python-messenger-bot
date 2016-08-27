from attachment import Button

class Template():
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
            assert all(type(button)==Button 
            	for button in self.kwargs['buttons']), "Missing type button"
            
            message['message']['attachment']['payload'] = {
                'template_type' : 'button',
                'text' : self.title,
                'buttons' : [b.to_json() for b in kwargs['buttons']]
            }
        
        elif self.type == self.generic_type:
        	# elements = kwargs.get('elements')
        	# TODO: Check types and check if elements exist in kwargs
            message['message']['attachment']['payload'] = {
                'template_type' : 'generic',
                'elements': kwargs['elements'].to_json()
            }
        
        elif self.type == self.receipt_type:
        	raise NotImplementedError

        return json.dumps(message)