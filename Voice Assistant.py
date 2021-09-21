import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'sun' in command:
                command=command.replace('sun','')
                print(command)
    except:
        pass
    return command


def run_sun():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is '+time)
    elif 'wikipedia' in command:
        person=command.replace('wikipedia','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'name' in command:
        talk('I am Sun Voice Assistant')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'home' in command:
        talk('Web is my home')
    elif 'terminate' in command:
        talk('Terminating the session')
        exit()
    else:
        talk('Please repeat')

while True:
    run_sun()