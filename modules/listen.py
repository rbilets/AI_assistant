import speech_recognition as sr
from modules.talk import talk


def listen():
    voice_rec = sr.Recognizer()

    with sr.Microphone() as source:
        # voice_rec.pause_threshold = 0
        voice_rec.adjust_for_ambient_noise(source, duration=.15)
        audio = voice_rec.listen(source)

        try:
            command = voice_rec.recognize_google(audio)
            print(f'You said {command} \n')
        except sr.UnknownValueError:
            talk('Sorry, I did not get it. Repeat again.')
            command = listen()
    return command.lower()
