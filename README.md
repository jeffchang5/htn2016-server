Mobile QuickStart
===

This repository is located at [https://github.com/twilio/mobile-quickstart](https://github.com/twilio/mobile-quickstart).

This repository includes server-side web application required for Twilio mobile sample apps such as QuickStart and BasicPhone. The Python script is responsible for generating capability tokens to clients and serving TwiML to Twilio.

Prerequisites
---

Please [sign up](https://www.twilio.com/try-twilio) for a free Twilio account. You will need your Account SID and Auth Token available in your [Account Dashboard](https://www.twilio.com/user/account/). You will also need to create a Twilio Application. Visit the [Apps tab](https://www.twilio.com/user/account/apps) to create an Application. Please make sure that you point the applications's Voice Request URL to your web application's public URL, e.g.,  http://companyfoo.com/call.
You will also need a verified phone number to be used as caller ID when placing phone calls.  See the "Verified Numbers" section
under the [Numbers](https://www.twilio.com/user/account/phone-numbers)
tab in your Twilio Account.

Deployment
---

In order to Twilio can communicate with your web application, it needs to be
deployed on the public Internet. You can run the application locally and
tunnel it using [ngrok](https://ngrok.com/). Alternatively, you can
deploy to [Heroku](https://heroku.com/):

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Please enter your Twilio Account Sid, Auth token, application sid and verified phone number.

If you prefer to deploy your application locally, please make sure that you have Python and `pip` installed. Please install the required packages:

    pip install -r requirements.txt

Please replace `ACCOUNT_SID`, `AUTH_TOKEN`, `APP_SID` and `CALLER_ID` in `server.py` with values from your Twilio account.  Simply run the application by `python server.py`.  You can tunnel `localhost` to the public Internet using ngrok: 

    ngrok 5000

Testing
---

Assuming that you are hosting the web application at http://companyfoo.com, open http://companyfoo.com/token in your browser. You should see a long string.

Client Configuration
---

Please modify BasicPhone and QuickStart to point to your web applications's public URL.


Usage
---

When the client starts, it connects to http://companyfoo.com/token to retrieve its capability token.

When you hit the "Call" button in the app, it will then make a call to your Twilio application that then makes a request to your web server (http://companyfoo.com/call)).  The script routes the call accordingly, either to a phone number or to another client. 

Please set up a Twilio phone number to point to your web application's public URL (http://companyfoo.com/call). When someone calls your Twilio number, Twilio makes a request to your web application.  The application routes the call to client `jenny`. Either a purchased number or your sandbox number can be used.
