import requests

from resources.urls import FACEBOOK_MESSAGES_POST_URL

class HttpClient():
    """
    Client which excutes the call to 
    facebook's messenger api
    """

    def submit_request(path, method, payload, headers):
        assert len(path) > 0
        if method == 'GET':
            raise NotImplementedError
        elif method == 'POST':
            raise NotImplementedError
