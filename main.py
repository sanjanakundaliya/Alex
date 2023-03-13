import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    # engine.say("I am Alexa's twin brother alex ")
    # engine.say("What can I do for You")
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...........")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                print(command)
    except:
        pass
    return command