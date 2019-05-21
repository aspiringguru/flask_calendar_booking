

from twilio.rest import Client

import config
client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+61488851653',
                     to='+61488851653'
                 )

print(message.sid)
