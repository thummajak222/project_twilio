import twilio
#print(twilio.__version__)

from twilio.rest import Client
#from moduleName.folder import class name

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACa1727f774839469253f90d1f5be60b3a'
auth_token = 'db2c76932a9f084125a88b7acc08f6ae'
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+66944013941", 
    from_="+12013358436",
    body="Thammachak Yotwichian (5805001426)")

print(message.sid)