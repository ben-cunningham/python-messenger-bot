from attachment import Button

receipt_properties = [
    'recipient_name',
    'order_number',
    'currency',
    'payment_method',
    'order_url',
    'timestamp',
    'address',
    'summary',
    'adjustments',
]


class Template(object):
    """
    Facebook Messenger message
    model for structured messages
    """
    button_type = 'button',
    generic_type = 'generic',
    receipt_type = 'receipt',
    
    types = {
        button_type,
        generic_type,
        receipt_type,
    }

    
    def __init__(self, type, **kwargs):
        self.type = type
        self.kwargs = kwargs

        if type not in self.types:
            raise ValueError("Incorrect type param: ", type)

        if self.type == self.receipt_type:            
            if any(kwarg not in receipt_properties for kwarg in self.kwargs):
                raise ValueError("Incorrect keyword-argument given")
        
        if 'buttons' in self.kwargs:
            if not all(isinstance(button, Button) 
                for button in kwargs['buttons']):
                    raise TypeError("Buttons list contained non-type Button")    

    def to_json(self):
        payload = {}

        if self.type == self.button_type:

            buttons = self.kwargs['buttons']
            buttons = [b.to_json() for b in buttons]

            payload = {
                'template_type': 'button',
                'text': self.kwargs['title'],
                'buttons': buttons
            }

        elif self.type == self.generic_type:
            # elements = kwargs.get('elements')
            # TODO: Check types and check if elements exist in kwargs
            elements = self.kwargs['elements']
            elements = [element.to_json() for element in elements]

            payload = {
                'template_type': 'generic',
                'elements': elements
            }

        elif self.type == self.receipt_type:
            payload = {
                'template_type': 'receipt'
            }

            elements = [element.to_json() for element in self.kwargs['elements']]
            payload['elements'] = elements

            for prop in receipt_properties:
                if prop in self.kwargs:
                    payload[prop] = self.kwargs[prop]

        return payload
