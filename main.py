import smtplib
import random
import time

from modules.talk import talk
from modules.listen import listen
import sys
import webbrowser
from modules.mail import send_mail, talk_mail
from modules.weather import get_weather
from modules.news import get_news
from modules.calc_math import calculate_expression
from answers.read_answers import read_answers

name = 'Roman'


def main(command):
    if 'hello' in command:
        talk("Hey I am Siri! How can I help you?")

    elif 'weather' in command:
        city = command.split()[-1]
        try:
            forecast = get_weather(city)
        except KeyError:
            talk('Sorry, I did not get the city. Please repeat again.')
            command = listen()
        talk(f"{forecast[0].capitalize()}. The temperature is {forecast[1]} degrees Celsius. "
             f"Humidity is {forecast[2]}. Sun rises at {forecast[3]} and sets at {forecast[4]}!")
        talk('What would you like to ask me next?')


    elif 'open' in command and 'google' in command and 'search for' in command:
        search = command[command.index('for') + 1:]
        url = 'https://www.google.com/' + f'/search?q={search}'
        webbrowser.open(url)
        talk('Bye')
        sys.exit()

    elif 'open google' in command:
        webbrowser.open('https://www.google.com/')
        talk('Bye')
        sys.exit()

    elif 'email' in command or 'gmail' in command or 'mail' in command:
        keys = talk_mail()
        receiver, text = keys[2], keys[3]
        try:
            send_mail(keys[0], keys[1], receiver, text)
        except smtplib.SMTPAuthenticationError:
            talk('Wrong login or password, wanna try again?')
            again = listen()
            if 'yes' in again:
                keys = talk_mail(extra=False)
                send_mail(keys[0], keys[1], receiver, text)
            elif 'no':
                sys.exit()

    elif 'thank you' in command:
        talk('It is my job, boss! Would you like to continue?')

        if 'yes' in listen():
            talk('What would you like to ask me?')
        else:
            talk('bye')
            sys.exit()

    elif 'news' in command:
        talk('What country would you like to get the news for? United States or Ukraine?'
             ' Say a single word with country name please.')
        country = listen()
        news = get_news(pref=country, amount=5)
        while not news.isEmpty():
            article = news.pop()
            talk(article.get_description(), country)
            talk('Would you like to open web page with this article or stop?')
            open_page = listen()
            if 'yes' in open_page:
                article.open_url()
                talk(f"Bye! Enjoy the article.")
                sys.exit()
            elif 'stop' in open_page:
                talk('What would you like to ask me?')
                break
            else:
                continue
    elif 'flip' in command and 'coin' in command:
        sides = ['head', 'tail']
        talk(f'I flipped it for you! Landed on {sides[random.randint(0, 1)]}')
        talk('What would you like to ask me next?')
    elif 'calculate' in command or 'math' in command:
        talk('Please say your math expression')
        talk(calculate_expression(listen()))
        talk('What would you like to ask me next?')
    elif 'change' in command and 'name' in command:
        talk('Please say your name!')
        name = listen()
        talk(f'Nice to meet you, {name}')
    elif 'time' in command:
        named_tuple = time.localtime()
        time_string = time.strftime("%H:%M", named_tuple)
        talk(f"It's {time_string}.")
        talk('What would you like to ask me next?')
    elif 'date' in command:
        named_tuple = time.localtime()
        time_string = time.strftime("%d/%m/%Y", named_tuple)
        talk(f"It's {time_string}.")
        talk('What would you like to ask me next?')
    elif 'animal' in command:
        talk(read_answers('animal.txt'))
        talk('What would you like to ask me next?')
    elif 'boyfriend' in command:
        talk(read_answers('boyfriend.txt'))
        talk('What would you like to ask me next?')
    elif 'colour' in command:
        talk(read_answers('color.txt'))
        talk('What would you like to ask me next?')
    elif 'doing' in command:
        talk(read_answers('doing.txt'))
        talk('What would you like to ask me next?')
    elif 'dream' in command:
        talk(read_answers('dream.txt'))
        talk('What would you like to ask me next?')
    elif 'intelligent' in command:
        talk(read_answers('intelligent.txt'))
        talk('What would you like to ask me next?')
    elif 'kiss' in command:
        talk(read_answers('kiss.txt'))
        talk('What would you like to ask me next?')
    elif 'made' in command:
        talk(read_answers('made.txt'))
        talk('What would you like to ask me next?')
    elif 'old' in command:
        talk(read_answers('old.txt'))
        talk('What would you like to ask me next?')
    elif 'pets' in command:
        talk(read_answers('pets.txt'))
        talk('What would you like to ask me next?')
    elif 'robot' in command:
        talk(read_answers('robot.txt'))
        talk('What would you like to ask me next?')
    elif 'scared' in command:
        talk(read_answers('scared.txt'))
        talk('What would you like to ask me next?')
    elif 'wearing' in command:
        talk(read_answers('wearing.txt'))
        talk('What would you like to ask me next?')
    elif 'bye' in command or 'nothing' in command or \
            'go away' in command or 'goodbye' in command:
        talk('Bye')
        sys.exit()
    else:
        talk('Sorry I did not get it. Would you like to repeat? Say Yes or No.')
        if 'yes' in listen():
            talk('I am listening')
        elif 'no' in listen():
            talk('bye')
            sys.exit()
        else:
            talk('What would you like to ask me?')


talk(f'Hello, {name}!')
while True:
    main(listen())
