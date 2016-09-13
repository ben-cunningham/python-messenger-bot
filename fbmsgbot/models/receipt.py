from attachment import Element

required_properties = {
    'price',
}


class ReceiptElement(Element):

    def __init__(self, quantity=None, price=None, 
                       currency="CAD", **kwargs):

        self.kwargs = kwargs
        super(ReceiptElement, self).__init__(**self.kwargs)
        
        if price is None:
                raise ValueError("Incorrect keyword-argument given for type ReceiptElement, needed: price") 
        
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
