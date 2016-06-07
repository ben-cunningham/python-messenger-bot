import requests

class HttpClient():
    """
    Client which excutes the call to 
    facebook's messenger api
    """

    def request_for_method(method, payload, headers):
        if method == 'GET':
            raise NotImplementedError
        elif method == 'POST':
            raise NotImplementedError
