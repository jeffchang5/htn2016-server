Mobile Quickstart
===

This repository is located at [https://github.com/twilio/mobile-quickstart](https://github.com/twilio/mobile-quickstart).

This repository includes server-side web application required for Twilio mobile sample apps such as Quickstart and BasicPhone. The Python script is responsible for generating capability tokens and serving TwiML.

Prerequisites
---

Please [sign up](https://www.twilio.com/try-twilio) for a free Twilio account. You will need your Account Sid and Auth Token available in your [Account Dashboard](https://www.twilio.com/user/account/). You will also need to create a [TwiML App](https://www.twilio.com/user/account/apps). Please make sure that you point the TwiML app's Voice Request URL to your web application's public URL, e.g.,  http://companyfoo.com/call.
You will also need a verified phone number to be used as caller ID when placing phone calls.  See the "Verified Caller Ids" section
under [Numbers](https://www.twilio.com/user/account/phone-numbers)
tab in your Twilio Account.

Deployment
---

In order to Twilio can communicate with your web application, it needs to be
deployed on the public Internet.  Some of the options include using [Heroku](https://heroku.com/), [ngrok](https://ngrok.com/), etc.

Click the button below to automatically set up the app using your Heroku account. Please enter your Twilio Account Sid, Auth token, TwiML App Sid and verified phone number when prompted.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

If you prefer to run your application locally, please make sure that you have Python and `pip` installed. Please install the required packages:

    pip install -r requirements.txt

Please replace `ACCOUNT_SID`, `AUTH_TOKEN`, `APP_SID` and `CALLER_ID` in `server.py` with values from your Twilio account.  Simply run the application by `python server.py`.  You can tunnel `localhost` to the public Internet using `ngrok`: 

    ngrok 5000

Testing
---

Please open http://companyfoo.com/token in your browser. You should see a long string.


Client Configuration
---

Please modify BasicPhone and Quickstart to point to your web applications's public URL.


Usage
---

At launch, the client connects to http://companyfoo.com/token to retrieve its capability token.

When you hit the "Call" button in the mobile app, it makes a call to your Twilio application that then makes a request to your web server (http://companyfoo.com/call).  The script routes the call accordingly, either to a phone number or to another client. 

If you want to receive a phone call in your mobile app you need to have a Twilio phone number (https://www.twilio.com/user/account/phone-numbers/incoming).  Please configure the phone number's Voice Request URL to point to your web application's public URL (http://companyfoo.com/call). When someone calls your Twilio phone number, Twilio makes a request to your web application. Your web application returns TwiML that instructs Twilio to connect the phone call with client `jenny`. Either a purchased number or your sandbox number can be used.
