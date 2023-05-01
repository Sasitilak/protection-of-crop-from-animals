# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC628117f16dbf8672cc8ec06de5c1a36c"
auth_token = "ab2381c4b32731339cdf2630cb7b1a38"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="hi sasi",
  from_="+12708177503",
  to="+919603753214"
)

print(message.sid)