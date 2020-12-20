import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "<ENTER YOUR API>"
account_sid = "<ENTER YOUR API>"
auth_token = "<ENTER YOUR API>"

weather_params = {
    # Berlin location
    "lat": 52.532463963476914,
    "lon": 13.283046695105751,
    "appid": api_key,
    "exclude": "current,minutely, daily"
}

will_rain = False

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)
