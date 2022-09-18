import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
from datetime import datetime
from github import Github

# Speech Engine Initialization

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
activationWord = "jarvis"

# Configure browser used

firefox_path = r"/Applications/Firefox.app/Contents/MacOS/firefox"
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

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
        
        query = parseCommand().lower()
            
        # List commands
       
        if 'look up' in query:
            speak('What would you like me to look up sir?')
            search_term = parseCommand()
            webbrowser.get('firefox').open_new(search_term)

        if query[0] == 'create' and query[1] == 'repo':
            g = Github("token")
            user = g.get_user()
            
            speak("What shall we name the repo sir?")
            repo_name = parseCommand()
            user.create_repo(repo_name)
