import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import TwilioRestClient
import requests
from dad_jokes import get_dad_joke

application = Flask(__name__)


@application.route('/dad', methods=['GET', 'POST'])
def incoming_sms():
    body = request.values.get('Body', None)

    resp = MessagingResponse()

    # determine message response
    if body.lower() == 'dad':
        resp.message(get_dad_joke())
    else:
        resp.message('Text "dad" to get a random dad joke')

    return str(resp)


if __name__ == "__main__":
    application.run(debug=True)
