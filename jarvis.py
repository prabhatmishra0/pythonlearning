from unittest import result
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser as web

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) # ye voice ko dikhyega ki Apke system me kaun si awaj hai
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# if __name__ == "__main__":
#     speak("jhgjhgjghgjh")

speak("I am Rinki Sir. Please tell me how may i help you")


def takeCommand():
    # It takes microphone input from the user the returns
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :  {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again pleases.....")
        return "None"
    return query


if __name__ == "__main__":
    query = takeCommand().lower()
    while True:

        # logic for excuting tasks based on query

        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accoerding to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            web.open("youtube.com")
