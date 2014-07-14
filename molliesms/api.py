"""\
Python implementation of the Mollie SMS Abstract Programming Interface
"""
from xml.dom.minidom import parseString
import types
import urllib
import urllib2

import molliesms.exceptions


class MollieSMS(object):
    """\
    The Mollie class allows you to send multiple sms messages using a single
    configuration. As an alternative, you can specify all arguments using the
    'sendsms' classmethod
    
    As per august 2014, old Mollie will not work anymore. All SMS services 
    have moved to Messagebird. Only secure call can be made to the SMS service.
    """
    DEFAULT_MOLLIEGW = "https://api.messagebird.com/xml/sms"
    SECURE_MOLLIEGW = "https://api.messagebird.com/xml/sms"

    DUTCH_GW = 1
    FOREIGN_GW = 2

    NORMAL_SMS = "normal"
    WAPPUSH_SMS = "wappush"
    VCARD_SMS = "vcard"

    def __init__(self, username, password, originator=None,
                 molliegw=None, gateway=None):
        """\
        Initialize the Mollie class. This configuration will be reused
        with each 'send' call.

        username
                authentication username
        password
                authentication password
        originator
                SMS originator phonenumber, i.e. +31612345678
        molliegw
                Full url of the Mollie SMS gateway. Two predefined
                gateways are available,

                MollieSMS.DEFAULT_MOLLIEGW
                    Standard (non secure) production gateway

                MollieSMS.Secure_MOLLIEGW
                    Secure production gateway (https)
        """
        self.username = username
        self.password = password
        self.originator = originator
        self.molliegw = molliegw or MollieSMS.DEFAULT_MOLLIEGW
        self.gateway = gateway or MollieSMS.FOREIGN_GW

    def send(self, recipients, message, originator=None, deliverydate=None,
             smstype=None, dryrun=False):
        """\
        Send a single SMS using the instances default configuration
        """
        originator = originator or self.originator

        return self.sendsms(self.username, self.password, originator,
               recipients, message, self.molliegw, self.gateway,
               deliverydate, smstype, dryrun)

    def sendsms(cls, username, password, originator, recipients,
                message, molliegw=None, gateway=None, deliverydate=None,
                smstype=None, dryrun=False):
        if type(recipients) not in (types.TupleType, types.ListType):
            recipients = [recipients]
        args = {}
        args['username'] = username
        args['password'] = password
        args['originator'] = originator
        args['recipients'] = ",".join(recipients)
        args['message'] = message
        molliegw = molliegw or MollieSMS.DEFAULT_MOLLIEGW

        # optional arguments

        url = molliegw + "?" + urllib.urlencode(args)
        if dryrun:
            print url
            return 0

        response = urllib2.urlopen(url)
        responsexml = response.read()
        dom = parseString(responsexml)
        recipients = int(dom.getElementsByTagName("recipients")[0].childNodes[0].data)
        success = dom.getElementsByTagName("success")[0].childNodes[0].data
        resultcode = int(dom.getElementsByTagName("resultcode")[0].childNodes[0].data)
        resultmessage = dom.getElementsByTagName("resultmessage")[0].childNodes[0].data

        if success != "true":
            e = molliesms.exceptions.by_code[resultcode]
            raise e(resultmessage)

        return recipients

    sendsms = classmethod(sendsms)
