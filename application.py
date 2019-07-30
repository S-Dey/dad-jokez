"""Dad joke generator"""
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from helpers import get_dad_joke

application = Flask(__name__)

"""route used for twilio phone number"""
@application.route('/dad', methods=['GET', 'POST'])
def incoming_sms():
    body = str(request.values.get('Body', type=str))

    resp = MessagingResponse()

    # determine message response
    if body.strip().lower() == 'dad':
        resp.message(get_dad_joke())
    else:
        resp.message('Text "dad" to get a random dad joke')

    return str(resp)


if __name__ == "__main__":
    application.run(debug=True)
