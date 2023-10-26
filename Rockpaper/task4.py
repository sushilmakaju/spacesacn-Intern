import pywhatkit as kit
from datetime import datetime

# whatsapp

# # Get the current time
# now = datetime.now()
# current_hour = now.hour
# current_minute = now.minute

# # Adjust the time for immediate delivery (within the next minute)
# current_minute += 1  # Add 1 minute to the current time

# # Recipient's WhatsApp number and message
# phone_number = "+9779840429631"  # Replace with the recipient's phone number
# message = " WhatsApp message"

# # Send the message immediately
# kit.sendwhatmsg(phone_number, message, current_hour, current_minute)

#sms
from twilio.rest import Client

# Twilio account information
account_sid = "ACae32e19ff9eb5cfda9deca61bef96900"
auth_token = "26e6ea2ee796e32bb159488794d31829"
client = Client(account_sid, auth_token)

# Send an SMS
to_phone_number = "+9779845352703"  # Replace with the recipient's phone number
from_phone_number = "+9779840429631"  # Your Twilio phone number
message = "This is an SMS sent from Python using Twilio."

client.messages.create(
    body=message,
    from_=from_phone_number,
    to=to_phone_number
)