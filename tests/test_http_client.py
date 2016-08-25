import unittest

import httpretty

from fbmsgbot.http_client import HttpClient
from fbmsgbot.resources.urls import FACEBOOK_MESSAGES_POST_URL


class TestHttpClient(unittest.TestCase):
    """
    Test the HttpClient
    """

    @httpretty.activate
    def test_submit_GET_request(self):

        httpretty.register_uri(httpretty.GET,
            FACEBOOK_MESSAGES_POST_URL + '/users/123',
            body='{ \
                "data" : [1,2,3] \
            }', status=200)

        client = HttpClient('123123')
        response, error = client.submit_request('/users/123', 
                                                'GET', None)

        assert response['data'] == [1, 2, 3]
        assert response['data'] != [3, 2, 1]

    @httpretty.activate
    def test_submite_POST_request(self):

        httpretty.register_uri(httpretty.POST,
            FACEBOOK_MESSAGES_POST_URL + 'users/',
            body='{ \
                "name": "ben", \
                "age": 12 \
            }', status=201)

        client = HttpClient('123123')
        response, error = client.submit_request('users/', 
                                                'POST', None)
        
        if error is None:
            assert response['name'] == 'ben'
            assert response['age'] == 12
        else:
            raise

