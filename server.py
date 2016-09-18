import os
from flask import Flask, request
from twilio.rest import TwilioRestClient
import cStringIO
import json
import phonenumbers
import tinys3

# Account Sid and Auth Token can be found in your account dashboard
ACCOUNT_SID = 'ACb0cacf43e157a1ec57ca591fa3fdbcf4'
AUTH_TOKEN = '72ac923817baa54a6a8be2b30c334335'


account_sid = os.environ.get("ACCOUNT_SID", ACCOUNT_SID)
auth_token = os.environ.get("AUTH_TOKEN", AUTH_TOKEN)
client = TwilioRestClient(account_sid, auth_token)


app = Flask(__name__)
@app.route('/text/<number>', methods=['POST'])
def text(number):
  content = request.get_data()
  content = json.loads(content)
  phone = phonenumbers.parse(content['phoneNumber'], "US")
  phone = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL).encode('ascii','ignore')

  vCard= cStringIO.StringIO()
  vCard.write("BEGIN:VCARD\n" +
              "VERSION:3.0\n")
  vCard.write('N:' +
              content['familyName'] + ';' +
              content['givenName'] + '\n' +
            "TEL;TYPE=CELL:" + number + '\n')
  vCard.write('END:VCARD')
  vCard.seek(0, os.SEEK_END)
  print(vCard.tell())
  connection = tinys3.Connection("AKIAJX63QUBTZGQ2A7IA", "bj8giuj4AWoxUMi0qGE4hII/8JF8MyJ1TvSm0GvV", default_bucket="twilio-contacts")
  file = content['givenName'] + content['familyName'] + '.vcf'
  connection.upload(file, vCard)
  client.messages.create(
          to = phone,
        from_ = "+12267740479",
        body = content['givenName'] + '\'s contact information!',
                              media_url = "http://twilio-contacts.s3.amazonaws.com/" + file,
  )

  return("Success!")



@app.route('/', methods=['GET', 'POST'])
def welcome():
  return "This is a Twilio API"

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
