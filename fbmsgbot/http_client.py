import requests, json

from resources.urls import FACEBOOK_MESSAGES_POST_URL


class HttpClient():
    """
    Client which excutes the call to
    facebook's messenger api
    """

    def __init__(self, api_token):
        self.api_token = api_token

    def submit_request(self, path, method, payload, completion):

        assert len(path) > 0
        
        path = self.get_api_url(path)
        headers = self.get_headers()

        if method == 'GET':
            response = requests.get(path, headers=headers)

            if response.status_code is not 200:
                error = self.get_error_from_response(response)
                completion(None, error)
            else:
                json_ = self.get_json(response.text)
                completion(json_, None)

        elif method == 'POST':
            response = requests.post(path, data=payload, headers=headers)

            if response.status_code is not 201:
                error = self.get_error_from_response(response)
                completion(None, error)
            else:
                json_ = self.get_json(response.text)
                completion(json_, None)


    def get_error_from_response(self, response):

        return {
            'error': self.get_json(response.text)
        }

    def get_json(self, string):

        return json.loads(string)

    def get_api_url(self, path):
        url = FACEBOOK_MESSAGES_POST_URL + path
        url = url + '?access_token=%s' % self.api_token

        return url

    def get_headers(self):
            
        return {}
