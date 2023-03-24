import os
import smtplib

EMAIL_ADDRESS = os.environ.get('USER_EMAIL')
EMAIL_PASSWORD = os.environ.get('USER_PASS')

with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
# with smtplib.SMTP('localhost' , 1025) as smtp:
     smtp.ehlo()
     smtp.starttls()
     smtp.ehlo()
     
     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
     
     subject = 'Grab dinner this weekend'
     body = 'How about dinner at 6pm this Saturday?'
     
     msg = f'Subject: {subject} \n\n {body}'
     
     smtp.sendmail(EMAIL_ADDRESS , 'rajasamkhan1@gmail.com', msg )

    
    