# from twilio.rest import TwilioRestClient
# https://github.com/twilio/twilio-python/tree/master/twilio/rest
from twilio import rest

account_sid = "AC1215028806334744afbc76a8ab8ce699" # Your Account SID from www.twilio.com/console
auth_token  = "f34bf30dded2af439e65f7b382e9e854"  # Your Auth Token from www.twilio.com/console

# client = TwilioRestClient(account_sid, auth_token)
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+818084913029",    # Replace with your phone number
    from_="+12564742282") # Replace with your Twilio number

print(message.sid)
