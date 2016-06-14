from http_client import HttpClient

class Bot():
    """
    @breif Facebook messenger bot
    """

    def __init__(self, token):
        self.api_token = token
        self.client = HttpClient()

    def send_message(self, message, completion):

        def _completion(response, error):
            print error
            if error is None:
                # TODO: Is there anything the bot needs to do?
                # maybe retry if it fails...?
                pass
            else:
                print response
                completion(response)

        self.client.submit_request('/me/messages', 
            'POST', 
            message.to_json(), 
            _completion)

    def set_welcome(self, message, completion):
        url = "/me/thread_settings?access_token=%s" % (self.access_token)
        
        def _completion(response, error):
            print error
            if error is None:
                # TODO: Is there anything the bot needs to do?
                # maybe retry if it fails...?
                pass
            else:
                print response
                completion(response)
        
        self.client.submit_request(
            url,
            'POST'
            message.to_json(),
            _completion)
        
