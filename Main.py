import operator
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import webbrowser
import wikipedia  # pip install wikipedia
import os
import smtplib
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('#username', '#password')
    server.sendmail('#username', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        if 1:
            query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)



        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
            speak("opening facebook")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("opening youtube")

        elif 'open instagram' in query:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com/")

        elif 'open thunkable' in query:
            speak("Opening Thunkable")
            webbrowser.open("https://x.thunkable.com/projects")

        elif 'roblox' in query:
            speak("Opening Roblox")
            webbrowser.open("https://web.roblox.com/home")

        elif 'open white hat dashboard' in query:
            speak("Opening White Hat Dashboard")
            webbrowser.open("https://code.whitehatjr.com/s/dashboard")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening stack overflow, need some help, do we sir?")

        elif 'go to sleep' in query:
            speak("bye sir")
            quit()

        elif 'thank you very much' in query:
            speak('Its my job to help you sir, is there anything else I can help you with?')

        elif 'no thank you' in query:
            speak('ok sir, I will wait for the next time I am needed')

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "bedazzle06@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'open my mail account' in query:
            speak("opening your mail account")
            webbrowser.open("https://mail.google.com/mail/u/2/#inbox")

        elif 'open my sister mail account' in query:
            speak("opening your sisters mail account")
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")

        elif 'open my dad mail account' in query:
            speak("opening daddy mail account")
            webbrowser.open("https://mail.google.com/mail/u/3/#inbox")

        elif 'open netflix' in query:
            speak("Let's Netflix And Chill")
            webbrowser.open("https://www.netflix.com/browse")

        elif 'open prime video' in query:
            speak("I don't like Prime video but okay")
            webbrowser.open("https://www.primevideo.com/region/eu/ref=av_auth_return_redir")

        elif 'open amazon' in query:
            speak("Opening Amazon. Let's do some window shopping!")
            webbrowser.open("https://www.amazon.in/ref=nav_logo")

        elif 'I have nothing to do' in query:
            speak("What do you think I do all the time staring at you!!!")

        elif 'shut up' in query:
            speak("Sorry Sir")

        elif 'good night' in query:
            speak("sweet dreams sir, remember to get up early")
            quit()

        elif 'how do I look' in query:
            speak("you're handsome as always, sir")

        elif 'tell me my future' in query:
            speak("you will be a pro coder")

        elif 'hello' in query:
            speak("yes sir?")

        elif 'open my playlist' in query:
            print("Opening your song playlist, sir")
            speak("Opening Your Playlist, Sir")
            webbrowser.open("https://www.youtube.com/watch?v=hXQxSi34GWY&list=RDMMhXQxSi34GWY&start_radio=1")

        elif 'open twitter' in query:
            print("opening twitter")
            speak("opening twitter")
            webbrowser.open("https://twitter.com/home")

        elif "tell me the temperature" in query:
            search = "temperature in Greater Noida"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak({f"current {search} in {temp}"})

        elif "internet speed" in query:
            import speedtest

            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir, we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
            print(f"sir, we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

        elif "tell me" in query:
            speak ("")

        elif "what is the battery" in query:
            import psutil

            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir, we have{percentage} percent battery left ")
            if percentage >= 75:
                speak("we have enough power to continue our work")
            elif percentage >= 40:
                speak("we should connect our system to charging point")
            elif percentage <= 15 and percentage <= 30:
                speak("we don't have enough power to work, please connect to charging")
            elif percentage <= 15:
                speak("we have very low battery, please connect to charging or the system will shut down very soon!")

        elif "turn on calculator mode" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Calculator mode is activated, please tell me what do you want to know")
                print("Calculator mode is activated, please tell me what do you want to know")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)


            def get_operator_fn(op, operator__truediv__=None):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'divided': operator__truediv__,
                }[op]


            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)


            speak("Your results is")
            speak(eval_binary_expr(*(my_string.split())))

        #how to do mode feature
        elif "activate how to do mode" in query:
            speak("How to do mode is activated, please tell me what do you want to know")
            how = takeCommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
