import smtplib
from modules.talk import talk
from modules.listen import listen


def send_mail(login, password, receiver, text):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(login, password)
    mail.sendmail(login, receiver, text)
    mail.close()


def talk_mail(extra=True):
    talk('Please type your login: ')
    login = input('Login: ')
    talk('Please type your password: ')
    password = input('Password: ')
    if extra:
        talk('Please type whom you would like to send the email to: ')
        receiver = input('Receiver: ')
        talk('What message would you like to send?')
        text = listen()
        return login, password, receiver, text
    return login, password