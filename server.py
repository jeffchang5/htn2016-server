import os
from flask import Flask, request
from twilio.rest import TwilioRestClient
# Account Sid and Auth Token can be found in your account dashboard
ACCOUNT_SID = 'ACb0cacf43e157a1ec57ca591fa3fdbcf4'
AUTH_TOKEN = '72ac923817baa54a6a8be2b30c334335'


account_sid = os.environ.get("ACCOUNT_SID", ACCOUNT_SID)
auth_token = os.environ.get("AUTH_TOKEN", AUTH_TOKEN)
client = TwilioRestClient(account_sid, auth_token)


app = Flask(__name__)
@app.route('/text/<number>', methods=['POST'])
def text(number):
  content = request.get_json(silent=True)
  print(content)
  message = client.messages.create(to=number, from_="+12267740479",
                                   body="Hello there!")




@app.route('/', methods=['GET', 'POST'])
def welcome():
  return "This is a Twilio API"

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
