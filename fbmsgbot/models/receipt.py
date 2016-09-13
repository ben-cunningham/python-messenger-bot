from attachment import Element

class ReceiptElement(Element):

    def __init__(self, quantity=None, price=None, 
                       currency="", **kwargs):

        assert quantity
        assert price
        assert currency

        self.kwargs = kwargs
        super(ReceiptElement, self).__init__(**self.kwargs)
        
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
