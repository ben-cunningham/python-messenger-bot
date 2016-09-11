import json
from http_client import HttpClient
from models.message import ReceivedMessage


class Bot():
    """
    @brief Facebook messenger bot
    """

    def __init__(self, token):

        self.api_token = token
        self.client = HttpClient(token)

    def send_message(self, message, recipient):

        payload = {
            'recipient': {
                'id': recipient,
            },
            'message': message.to_json()
        }

        payload = json.dumps(payload)

        response, error = self.client.submit_request(
                            '/me/messages',
                            'POST',
                            payload)

        if error is not None:
            print 'Error Encountered! Could not send message\n'
            print 'Message: %s' % error

        return response, error

    def set_welcome(self, message):

        greeting = {
            'setting_type': 'greeting',
            'greeting': {
                'text': message
            }
        }

        data = json.dumps(greeting)

        response, error = self.client.submit_request(
            '/me/thread_settings',
            'POST',
            data)

        return response, error

    def messages_for_request(self, request):
        """
        Handle incoming requests from the webhook
        """

        entries = request.json['entry']
        messages = []
        for entry in entries:
            for msg in entry['messaging']:
                if msg.get('message') and msg['message'].get('text'):
                    messages.append(ReceivedMessage(msg))

        return messages

    def message_from_reciept(receipt):
        """
        Handle receipts
        """

        raise NotImplementedError

    def set_persistent_menu(self, buttons):
        """
        Sets the persistent menu. 
        @params: buttons -> list of button objects
        @moreinfo: https://developers.facebook.com/docs/messenger-platform/thread-settings/persistent-menu
        """

        payload = {
            "setting_type": "call_to_actions",
            "thread_state": "existing_thread",
            "call_to_actions": [    
                button.to_json() for button in buttons
            ]
        }
        
        data = json.dumps(payload)
        response, error = self.client.submit_request(
            '/me/thread_settings',
            'POST',
             data)

        return response, error

