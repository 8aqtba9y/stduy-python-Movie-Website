# from twilio.rest import TwilioRestClient
# https://github.com/twilio/twilio-python/tree/master/twilio/rest
from twilio import rest

account_sid = "XXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxx" # Your Account SID from www.twilio.com/console
auth_token  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Your Auth Token from www.twilio.com/console

# client = TwilioRestClient(account_sid, auth_token)
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+xxxxxxxxxxxx",    # Replace with your phone number
    from_="+xxxxxxxxxxxx") # Replace with your Twilio number

print(message.sid)
