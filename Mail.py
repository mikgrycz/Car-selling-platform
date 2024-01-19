import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_car_details(recipient_email):
    # Set up the SMTP server
    smtp_server = smtplib.SMTP(os.getenv('SERVER_MAIL'), 587)
    smtp_server.starttls()
    smtp_server.login(os.getenv('SERVER_MAIL'),os.getenv('SERVER_PASSWORD'))

    # Create the message
    message = MIMEText(f'Car details:\n\n')
    message['Subject'] = 'Car Details'
    message['From'] = os.getenv('SERVER_MAIL')
    message['To'] = recipient_email

    # Send the message
    smtp_server.send_message(message)
    smtp_server.quit()

