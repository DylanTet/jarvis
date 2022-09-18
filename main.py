import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
from datetime import datetime

# Speech Engine Initialization

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
activationWord = "jarvis"

def speak(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

# Function to listen to voice through computer microphone and turn it to text

def parseCommand():
    listener = sr.Recognizer()
    print('Listening...')
    
    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)
        
    try:
        print('Parsing Words...')
        query = listener.recognize_google(input_speech, language='en_gb')
        print('The command was: ' + query)    
    except Exception as exception:
        print('I did not recognize your command')
        speak('I did not understand the command sir')
        print(exception)
        return 'None'
    return query

# Main loop

if __name__ == '__main__':
    speak('All systems nominal sir.')
    
    while True:
        # Parsing the query input and putting it into an array or list
        
        query = parseCommand().lower().split()
        
        if query[0] == activationWord:
            query.pop(0)
            
            # List commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings, sir')
                else:
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)
            