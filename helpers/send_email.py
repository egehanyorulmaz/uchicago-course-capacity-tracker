# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config.credentials import SMTP_API_KEY

message = Mail(
    from_email='XX@gmail.com',
    to_emails='egehanyorulmaz@gmail.com',
    subject='Your section has now available spots!',
    html_content='<strong>Your course has now available sections that you might be interested in!</strong>')
try:
    sg = SendGridAPIClient(SMTP_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)