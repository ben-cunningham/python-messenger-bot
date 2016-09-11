from attachment import Element

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

class ReceiptElement(Element):

    def __init__(self, quantity=None, price=None, 
                       currency="", **kwargs):

        self.kwargs = kwargs
        super(ReceiptElement, self).__init__(**self.kwargs)

        if any(kwarg not in receipt_properties for kwarg in self.kwargs):
                raise ValueError("Incorrect keyword-argument given")
        
        self.quantity = quantity
        self.price = price
        self.currency = currency


    def to_json(self):

        payload = {
            'title': self.title,
            'subtitle': self.subtitle,
            'quantity': self.quantity,
            'price': self.price,
            'currency': self.currency,
            'image_url': self.image_url
        }

        return payload
