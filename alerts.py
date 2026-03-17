from twilio.rest import Client

account_sid = "YOUR_SID"
auth_token = "YOUR_TOKEN"

client = Client(account_sid, auth_token)

def send_whatsapp(message, number):

    client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{number}'
    )