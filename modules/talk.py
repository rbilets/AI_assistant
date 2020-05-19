from gtts import gTTS
import pygame
import requests

requests.packages.urllib3.disable_warnings()


def talk(text, language='en-us'):
    print(text)
    text = str(text)
    if 'ukrain' in language:
        language = 'uk'
    else:
        language='en-us'

    text_to_speech = gTTS(text=text, lang=language)
    text_to_speech.save('audio.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

