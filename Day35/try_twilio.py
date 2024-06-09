
from dotenv import load_dotenv
from twilio.rest import Client

import os

load_dotenv()

from_phone = os.environ.get("TWILIO_PHONE")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=from_phone,
  body='Hello from Twilio, This is Eric',
  to='+19196234885'
)

print(message.sid)