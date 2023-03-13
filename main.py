import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes

import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


def talk(text):

    # engine.say("I am Alexaa's twin brother alex ")
    engine.say(text)
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
                command=command.replace('alex','')
                print(command)
    except:
        pass
    return command
def run_Alex():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk(time)
        print(time)
    elif 'who the heck is' in command:
        person=command.replace('who the heck is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('No I will not')
    elif 'single' in command:
        talk('Its none of your buisness')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('hey I cannot hear you properly')


while True:
    run_Alex()