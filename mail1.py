import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('USER_EMAIL')
EMAIL_PASSWORD = os.environ.get('USER_PASS')

contacts = ['rajasamkhan1@gmail.com' , 'i192024@nu.edu.pk']

msg = EmailMessage()
msg['Subject'] =  'Grab dinner this weekend'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
# msg['To'] =  'rajasamkhan1@gmail.com'
msg.set_content('How about dinner at 6pm this Saturday?')

files = ['DAA.pdf']

for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octate-stream', filename= file_name)

with smtplib.SMTP_SSL('smtp.gmail.com' , 465) as smtp: 
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)