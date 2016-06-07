import requests, json

from resources.urls import FACEBOOK_MESSAGES_POST_URL


class HttpClient():
    """
    Client which excutes the call to
    facebook's messenger api
    """

    def submit_request(self, path, method, payload, completion):

        assert len(path) > 0
        
        path = self.get_api_url(path)
        headers = self.get_headers()

        if method == 'GET':
            request = requests.get(path, headers=headers)

            if request.status_code is not 200:
                error = self.get_error_from_request(request)
                completion(None, error)
            else:
                json_ = self.get_json(request.text)
                completion(json_, None)

        elif method == 'POST':
            raise NotImplementedError

    def get_error_from_request(self, request):

        return {
            'error': self.get_json(request.text)
        }

    def get_json(self, string):

        return json.loads(string)

    def get_api_url(self, path):
            
        return FACEBOOK_MESSAGES_POST_URL + path

    def get_headers(self):
            
        return {}
