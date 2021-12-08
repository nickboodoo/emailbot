import smtplib
import pyttsx3
import sys
from email.message import EmailMessage


# Initialize text to speech engine
engine = pyttsx3.init()


# Function for engine to talk to the user
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Function to send an email from my email address
def send_email(recipient, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('SAMPLE@gmail.com', 'SAMPLE')

# Compiles email message from user input
    email = EmailMessage()
    email['From'] = 'SAMPLE@gmail.com'
    email['To'] = recipient
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


# Dictionary of contacts listed by date of birth
email_contacts = {
    '01/01/2001': 'SAMPLE@gmail.com',
}

# Dictionary of subjects
email_subjects = {
    '1': 'TOPIC 1',
    '2': 'TOPIC 2',
    '3': 'TOPIC 3',
    '4': 'TOPIC 4',
    '5': 'TOPIC 5'
}

# If statement locks unauthorized users out of the program
print('Hello, please enter your password.')
if input() == '0000':
    talk('Hello')

# Function to get the email composition from the user
    def get_email_info():
        talk('What is the patient\'s date of birth?')
        dob = input().lower()
        recipient = email_contacts[dob]

        print('Patient\'s Email Address: ' + recipient)

        talk('What is the subject of your email?')

        print('[1] TOPIC 1')
        print('[2] TOPIC 2')
        print('[3] TOPIC 3')
        print('[4] TOPIC 4')
        print('[5] TOPIC 5')

        topic = input().lower()
        subject = email_subjects[topic]

        print('Subject: ' + subject)

        talk('What is the body of your email?')
        message = input()

        print('Message: ' + message)

        talk('Alright, your email has been sent')
        print('Email successfully sent')

        talk('Would you like to send another email?')
        # While loop restarts or shuts down program
        while True:
            answer = input()
            if answer.lower().startswith('y'):
                get_email_info()
            elif answer.lower().startswith('n'):
                talk('OK, Goodbye')
                sys.exit()

# Executing function to run email loop
    get_email_info()


else:
    print('Sorry, that password was incorrect.')
    input()
