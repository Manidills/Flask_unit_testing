import unittest
from app import app
from xml.etree import ElementTree

class TwiMLTest(unittest.TestCase):
    def setUp(self):
        self.test_app = app.test_client()

    def assertTwiML(self, response):
        self.assertEquals(response.status, "200 OK")
        root = ElementTree.fromstring(response.data)
        self.assertEquals(root.tag, 'Response',
                "Did not find  tag as root element " \
                "TwiML response.")

    

    def message(self, body, url='/sms', to="+15550001111",
            from_='+15558675309', extra_params={}):


        params = {
            'MessageSid': 'SMtesting',
            'AccountSid': 'ACxxxxxxx',
            'To': to,
            'From': from_,
            'Body': body,
            'NumMedia': 0,
            'FromCity': 'TRY',
            'FromState': 'TN',
            'FromCountry': 'IND',
            'FromZip': '621601'}

        # Add extra params not defined by default.
        if extra_params:
            params = dict(params.items() + extra_params.items())

        # Return the app's response.
        return self.test_app.post(url, data=params)

class TestSms(TwiMLTest):
    def test_sms(self):
        response = self.message(url='/sms', body='Taylor swift')
        self.assertTwiML(response)

    def test_sms_valid(self):
       
        response = self.message(url='/sms',body='Taylor swift')

        
        root = ElementTree.fromstring(response.data)

        dial_query = root.findall('Dial')
        self.assertEquals(len(dial_query), 0,
                "Did not find one Dial verb, instead found: %i " %
                len(dial_query))

        
