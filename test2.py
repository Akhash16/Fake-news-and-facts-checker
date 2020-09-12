from twilio.rest import Client 
 
account_sid = 'AC599de24576901fd6aac1ed70ae500510' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello! This is an editable text message. You are free to change it and write whatever you like.',      
                              to='whatsapp:+917904594440' 
                          ) 
 
print(message.sid)