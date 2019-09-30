import pyttsx3
import  wikipedia
engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wiki(query):
     speak('Searching Wikipedia...')
     print('Searching Wikipedia...')
     query = query.replace("wikipedia", "")
     try:
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)
     except Exception as e:
        speak("oops! can't find relivent details")

def reading():
    file="text.txt"
    f=open(file,'r')
    for i in f:
        speak(i)

#n=input("SEARCH--->>>")
#wiki(n)
reading()