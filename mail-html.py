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
msg.set_content('This is a plain text email!')
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype = 'html')


with smtplib.SMTP_SSL('smtp.gmail.com' , 465) as smtp: 
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)