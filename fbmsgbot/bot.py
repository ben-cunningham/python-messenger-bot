from http_client import HttpClient

"""
@breif Facebook messenger bot
"""
class Bot():

    def __init__(self, token):
        self.api_token = token
        self.client = HttpClient()   

    def send_message(self, message):

        def completion(response, error):
            if error is None:
                # TODO: Is there anything the bot needs to do?
                # maybe retry if it fails...?
                pass
            else:
                pass

        self.client.submit_request('/me/messages', 
            'POST', 
            message.to_json(), 
            completion)

    def handle_incoming():
        raise NotImplementedError
