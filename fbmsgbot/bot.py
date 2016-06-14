from http_client import HttpClient

class Bot():
    """
    @breif Facebook messenger bot
    """

    def __init__(self, token):
        self.api_token = token
        self.client = HttpClient()

    def send_message(self, message, completion):

        def completion(response, error):
            if error is None:
                # TODO: Is there anything the bot needs to do?
                # maybe retry if it fails...?
                pass
            else:
                completion()

        self.client.submit_request('/me/messages', 
            'POST', 
            message.to_json(), 
            completion)
