from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()
import config
client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+15005550006'

client.messages.create(body='join talk-replied.',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
