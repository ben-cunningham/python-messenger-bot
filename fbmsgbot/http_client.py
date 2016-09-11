import requests
import json
from resources.urls import FACEBOOK_MESSAGES_POST_URL


class HttpClient():
    """
    Client which excutes the call to
    facebook's messenger api
    """

    def __init__(self, api_token):

        self.api_token = api_token

    def submit_request(self, path, method, payload):

        path = self.get_api_url(path)
        headers = self.get_headers()
        response = error = r = None

        if method == 'GET':
            r = requests.get(path, headers=headers)

        elif method == 'POST':
            r = requests.post(path, data=payload, headers=headers)

        if r.status_code < 300:
            response = self.get_json(r.text)

        else:
            r_error = self.get_error_from_response(r)
            response, error = r_error['message'], r_error['type']

        return response, error

    def get_error_from_response(self, response):

        return self.get_json(response.text)['error']

    def get_json(self, string):

        return json.loads(string)

    def get_api_url(self, path):

        url = FACEBOOK_MESSAGES_POST_URL + path
        url = url + '?access_token=%s' % self.api_token

        return url

    def get_headers(self):

        return {
            'content-type':  'application/json'
        }
