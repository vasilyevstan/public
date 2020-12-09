import os
import credentials as cred
from twilio.rest import Client


client = Client(cred.account_sid, cred.auth_token)

message = client.messages.create(
                              from_ = cred.sender,
                              body = 'Hello world!',
                              to = cred.receiver
                          )

print(message.sid)
