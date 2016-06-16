from http_client import HttpClient
 
from models.message import ReceivedMessage

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
                print 'Error Encountered! Could not send message\n'
                print 'Message: %s' % error
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

    def messages_for_request(self, request):
        """
        Handle incoming requests from the webhook
        """

        entries = request.json['entry']
        messages = []
        for entry in entries:
            message = {}
            for msg in entry['messaging']:
                messages.append(ReceivedMessage(msg))

        return messages

    def message_from_reciept(receipt):
        """
        Handle receipts
        """

        raise NotImplementedError
