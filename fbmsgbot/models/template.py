from attachment import Button

receipt_req_properties = {
    'recipient_name',
    'order_number',
    'currency',
    'payment_method',
    'elements',
    'summary',
}

receipt_not_req_props = {
    'timestamp',
    'order_url',
    'address',
    'adjustments',
}

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
        
        for attr, val in kwargs.iteritems():
            try:
                setattr(self, attr, val)
            except AttributeError as e:
                print e, attr, val
    
    @property 
    def buttons(self):
        return [b.to_json() for b in self._buttons]
    
    @buttons.setter
    def buttons(self, buttons):

        MAX_BUTTONS = 3
        button_count = len(buttons)
        
        if button_count > MAX_BUTTONS:
            # Check button count is with fb defined range
            # Could this be a better exception?
            raise ValueError(
                "Maximum buttons in template: %d." \
                "Found: %d" % (MAX_BUTTONS, button_count)
            )

        # Check each value of button list is indeed a button
        if not all(isinstance(button, Button) for button in buttons):
                raise TypeError("Buttons list contained non-type Button") 

        # Finall set value of 
        self._buttons = buttons 

    def update_button(self):
        
        payload = {
            'text': self.kwargs['title'],
            'buttons': self.buttons
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
       
        for _property in receipt_req_properties:
            if _property not in self.kwargs:
                raise ValueError("Incorrect keyword-argument given, needed: ", _property) 

        payload = {}
        elements = self.kwargs['elements']
        elements = [element.to_json() for element in elements]
        self.kwargs['elements'] = elements

        # Merge required and non req props
        for prop in receipt_req_properties | receipt_not_req_props:
            # Note.. given success of exception above I think
            # This if statement could be reduced
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
