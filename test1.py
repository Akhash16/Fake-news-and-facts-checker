from twilio.rest import Client 
 
account_sid = 'AC599de24576901fd6aac1ed70ae500510' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+917904594440' 
                          ) 
 
print(message.sid)