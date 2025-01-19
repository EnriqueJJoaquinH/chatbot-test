""" Sending message without template """

import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_num = os.getenv('TWILIO_NUM')
client_num = os.getenv('CLIENT_NUM')

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_ = f'whatsapp:{twilio_num}',
    body = 'Good morning',
    to = f'whatsapp:{client_num}'
)

print(message.sid)
