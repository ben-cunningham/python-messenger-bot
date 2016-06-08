import unittest, json

from pybot.models.attachment import Element, Button, WebUrlButton, PayloadButton

"""
Test Button
"""
class TestButton(unittest.TestCase):

    def test_constructor(self):
        weburl = WebUrlButton("Button title", "www.test.com")

        assert weburl.type == "web_url", 'WebUrl type failed'
        assert weburl.title == "Button title", "WebUrl title failed"
        assert weburl.url == "www.test.com", "WebUrl URL failed"

        payload = PayloadButton("Button title2", "USR_DEFINE")
        assert payload.type == "postback", "Payload type failed"
        assert payload.title == "Button title2", "Button title failed"
        assert payload.payload == "USR_DEFINE", "Button payload failed"

    def test_to_json(self):
        weburl = WebUrlButton("Button title", "www.test.com")
        payload = PayloadButton("Button title2", "USR_DEFINE")

        webjson = weburl.to_json()
        webjson = json.loads(webjson)
        assert webjson['type'] == "web_url", 'WebUrl type failed'
        assert webjson['title'] == "Button title", "WebUrl title failed"
        assert webjson['url'] == "www.test.com", "WebUrl URL failed"

        payloadjson = payload.to_json()
        payloadjson = json.loads(payloadjson)
        assert payloadjson['type'] == "postback", "Payload type failed"
        assert payloadjson['title'] == "Button title2", "Button title failed"
        assert payloadjson['payload'] == "USR_DEFINE", "Button payload failed"

class TestElement(unittest.TestCase):

    def test_element(self):
        weburl = WebUrlButton("Button title", "www.test.com")
        payload = PayloadButton("Button title2", "USR_DEFINE")
        button_list = [weburl, payload]
        element = Element("Grey Shirt", "www.greyshirt.com", "soft shirt", button_list)

        assert element.title == "Grey Shirt", "Element title error"
        assert element.image_url == "www.greyshirt.com", "Element URL error"
        assert element.subtitle == "soft shirt", "Element subtitle error"
        assert element.buttons == [weburl, payload], "Element buttons error"

    def test_element_json(self):
        weburl = WebUrlButton("Button title", "www.test.com")
        payload = PayloadButton("Button title2", "USR_DEFINE")
        button_list = [weburl, payload]
        element = Element("Grey Shirt", "www.greyshirt.com", "soft shirt", button_list)
        
        element_json = json.loads(element.to_json())
        assert element_json['title'] == "Grey Shirt"
        assert element_json['image_url'] == "www.greyshirt.com"
        assert element_json['subtitle'] == "soft shirt"
        assert weburl.to_json() in element_json['buttons']
        assert payload.to_json() in element_json['buttons']

        

