from http_client import HttpClient

class Bot():
    """
    @brief Facebook messenger bot
    """

    def __init__(self, token):
        self.api_token = token
        self.client = HttpClient(token)

    def send_message(self, message, completion):

        def _completion(response, error):
            if error is not None:
                pass
            else:
                completion(response)

        self.client.submit_request(
            '/me/messages', 
            'POST', 
            message.to_json(), 
            _completion)

    def set_welcome(self, message, completion):
        
        def _completion(response, error):
            if error is not None:
                pass
            else:
                completion(response)

        self.client.submit_request(
            '/me/thread_settings',
            'POST',
            message.to_json(),
            _completion)
        
