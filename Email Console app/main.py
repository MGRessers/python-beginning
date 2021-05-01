import smtplib
import json
import config

def send_email(subject, msg, send):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('bigdream66111@gmail.com' , 'Apple100.youtube')
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('bigdream66111@gmail.com' , send, message)
        server.quit()
        print("Email successfully sent.")
    except:
        print("Email failed to send.")

def main():
    print("1. Reset Email & Password")
    print("2. Send E-Mail")
    print("3. Exit")
    choice = int(input("Choose Menu :"))
    if(choice == 1):
        dele = input('Do you want to reset the set email and password (yes or no): ')
        if(dele == "yes"):

            print("Email and password reset, Restart the program.")
            config.EMAIL_ADDRESS = ""
            config.PASSWORD = ""
        
        else:

            subject = input("Enter your subject: ")
            message = input("Enter your message: ")
            send = input("Enter email of who you are sending to: ")
            send_email(subject, message, send)

    
    elif(choice == 2):

        if(config.EMAIL_ADDRESS and config.PASSWORD):
            subject = input("Enter your subject: ")
            message = input("Enter your message: ")
            send = input("Enter email of who you are sending to: ")
            send_email(subject, message, send)
        else:
            config.EMAIL_ADDRESS = input("Enter your email: ")
            config.PASSWORD = input("Enter your password: ")
            main()

    elif(choice == 3):
        quit()

    else:
        print("Error : There is no such option!")
        main()
main()

