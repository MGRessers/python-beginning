import smtplib
import config
import json

with open('data.json', 'r') as d:
 json.load(d)

if(config.EMAIL_ADDRESS and config.PASSWORD):
    dele = input('Do you want to reset the set email and password (yes or no): ')
    if(dele == "yes"):

        print("Email and password reset, Restart the program.")
        config.EMAIL_ADDRESS = ""
        config.PASSWORD = ""

    subject = input(str("Enter your subject: "))
    msg = input(str("Enter your message: "))
    send = input(str("Enter the email of who you are sending this to: "))
else:
    
    config.EMAIL_ADDRESS = input(str("Enter your email address you are using to send an email: "))
    config.PASSWORD = input(str("Enter the password of your email: "))
    subject = input(str("Enter your subject: "))
    msg = input(str("Enter your message: "))
    send = input(str("Enter the email of who you are sending this to: "))

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.SENDING_TO, message)
        server.quit()
        print("Email successfully sent.")
    except:
        print("Email failed to send.")

send_email(subject,msg)