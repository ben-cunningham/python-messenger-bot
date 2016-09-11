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
    button_type = 'button'
    generic_type = 'generic'
    receipt_type = 'receipt'
    
    types = {
        button_type,
        generic_type,
        receipt_type,
    }

    def __init__(self, type_, **kwargs):
        self.type = type_
        self.kwargs = kwargs

        if self.type not in self.types:
            raise ValueError("Incorrect type param: ", self.type)
    
    def update_button(self):
        
        buttons = self.kwargs['buttons']
        if not all(isinstance(button, Button) 
                for button in buttons):
                    raise TypeError("Buttons list contained non-type Button") 
        
        buttons = [b.to_json() for b in buttons]
        payload = {
            'text': self.kwargs['title'],
            'buttons': buttons
        }

        return payload
    
    def update_generic(self):
        
        elements = self.kwargs['elements']
        elements = [element.to_json() for element in elements]

        payload = {
            'elements': elements
        }

        return payload
    
    def update_receipt(self):
        
        if any(kwarg not in receipt_properties for kwarg in self.kwargs):
                raise ValueError("Incorrect keyword-argument given")
        
        elements = [element.to_json() for element in self.kwargs['elements']]
        payload = {
            'elements': elements
        }

        for prop in receipt_properties:
            if prop in self.kwargs:
                payload[prop] = self.kwargs[prop]

        return payload

    def to_json(self):
        
        payload = {
            'template_type': self.type
        }
        # Set a switch dict to avoid ugly if etc etc..
        switcher = {
            self.button_type: self.update_button,
            self.generic_type: self.update_generic,
            self.receipt_type: self.update_receipt,
        }
        # Update payload with corresponding function
        payload.update(
            switcher[self.type]()
        )

        return payload
