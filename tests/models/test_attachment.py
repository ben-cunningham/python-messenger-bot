import unittest, json

from fbmsgbot.models.attachment import Element, Button

"""
Test Button
"""
class TestButton(unittest.TestCase):

    def test_constructor(self):
        weburl = Button('web_url', "Button title", "www.test.com")

        assert weburl.type == "web_url", 'WebUrl type failed'
        assert weburl.title == "Button title", "WebUrl title failed"
        assert weburl.payload == "www.test.com", "WebUrl URL failed"

        payload = Button('postback', "Button title2", "USR_DEFINE")
        assert payload.type == "postback", "Payload type failed"
        assert payload.title == "Button title2", "Button title failed"
        assert payload.payload == "USR_DEFINE", "Button payload failed"

    def test_to_json(self):
        weburl = Button('web_url', "Button title", "www.test.com")
        payload = Button('postback', "Button title2", "USR_DEFINE")

        webjson = weburl.to_json()
        assert webjson['type'] == "web_url", 'WebUrl type failed'
        assert webjson['title'] == "Button title", "WebUrl title failed"
        assert webjson['url'] == "www.test.com", "WebUrl URL failed"

        payloadjson = payload.to_json()
        assert payloadjson['type'] == "postback", "Payload type failed"
        assert payloadjson['title'] == "Button title2", "Button title failed"
        assert payloadjson['payload'] == "USR_DEFINE", "Button payload failed"

class TestElement(unittest.TestCase):

    def test_element(self):
        weburl = Button('web_url', "Button title", "www.test.com")
        payload = Button('postback', "Button title2", "USR_DEFINE")
        button_list = [weburl, payload]
        element = Element("Grey Shirt", "soft shirt", "www.greyshirt.com",  button_list)

        assert element.title == "Grey Shirt", "Element title error"
        assert element.image_url == "www.greyshirt.com", "Element URL error"
        assert element.subtitle == "soft shirt", "Element subtitle error"
        assert element.buttons == [weburl, payload], "Element buttons error"

    def test_element_json(self):
        weburl = Button('web_url', "Button title", "www.test.com")
        payload = Button('postback', "Button title2", "USR_DEFINE")
        button_list = [weburl, payload]
        element = Element("Grey Shirt", "soft shirt", "www.greyshirt.com", button_list)
        
        element_json = element.to_json()
        assert element_json['title'] == "Grey Shirt"
        assert element_json['image_url'] == "www.greyshirt.com"
        assert element_json['subtitle'] == "soft shirt"
        assert weburl.to_json() in element_json['buttons']
        assert payload.to_json() in element_json['buttons']

        

