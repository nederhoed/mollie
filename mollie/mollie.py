
import urllib, urllib2
from xml.dom.minidom import parseString
import types

class Mollie:
    DEFAULT_MOLLIEGW="http://www.mollie.nl/xml/sms/"
    SECURE_MOLLIEGW="http://www.mollie.nl/xml/sms/"

    DUTCH_GW=1
    FOREIGN_GW=2

    def __init__(self, username, password, originator=None,
                 molliegw=None, gateway=None):
        self.username = username
        self.password = password
        self.originator = originator
        self.molliegw = molliegw or DEFAULT_MOLLIEGW
                 
    def send(self, recipients, message, originator=None, deliverydate=None,
             smstype=None):
             pass

    def sendsms(cls, username, password, originator, recipients, 
                message, molliegw, gateway=None, deliverydate=None, 
                smstype=None):
        if type(recipients) not in (types.TupleType, types.ListType):
            recipients = [recipients]
        args = {}
        args['username'] = username
        args['password'] = password
        args['originator'] = originator
        args['recipients'] = ",".join(recipients)
        args['message'] = message

        # optional arguments

        url = molliegw + "?" + urllib.urlencode(args)
        response = urllib2.urlopen(url)
        responsexml = response.read()
        responsedom = parseString(responsexml)
        recipients = dom.getElementsByTagName("recipients")[0].childNodes[0].data
        success = dom.getElementsByTagName("success")[0].childNodes[0].data
        resultcode = dom.getElementsByTagName("resultcode")[0].childNodes[0].data
        resultmessage = dom.getElementsByTagName("resultmessage")[0].childNodes[0].data
    sendsms = classmethod(sendsms)
