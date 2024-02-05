import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

def send_text(message, carrier='att'):
    recipient = f'{PHONE_NUMBER}{CARRIERS[carrier]}'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
 
    server.sendmail(EMAIL, recipient, message)
 

if __name__ == '__main__':
    send_text("testing...")
