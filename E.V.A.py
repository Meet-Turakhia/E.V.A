import os
import pyowm
import pyjokes
import pyttsx3
import smtplib
import datetime
import wikipedia
import webbrowser
from selenium import webdriver
import speech_recognition as sr
from newsapi import NewsApiClient
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyaudio
import requests
import json
from goodreads_quotes import Goodreads
from quote import quote
from quotes import Quotes
import wikiquote
import plyer
import schedule
import datetime
import winshell
import psutil
import platform
import screen_brightness_control as sbc
import re

# p = pyaudio.PyAudio()
# info = p.get_host_api_info_by_index(0)
# numdevices = info.get('deviceCount')
# for i in range(0, numdevices):
#     if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
#         print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))


# initializing the pyttsx3 for text to speech conversion
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    # function for text to speech
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # takes microphone input and returns string as output
    r = sr.Recognizer()
    with sr.Microphone(1) as source:
        print("Listening.../")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Recognizing.../")
        query = r.recognize_google(audio, language="en-in")
        print(f"You: {query} <-")
    except Exception as e:
        # print("E.V.A: Sorry could not catch that, can you rephrase please?")
        # speak("sorry could not catch that, can you rephrase please")
        return "None"
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("E.V.A: Good Morning! <-")
        speak("good morning")
    elif hour >= 12 and hour < 18:
        print("E.V.A: Good Afternoon! <-")
        speak("good afternoon")
    elif hour >= 18 and hour < 21:
        print("E.V.A: Good Evening! <-")
        speak("good evening")
    print("E.V.A: Hello I am E.V.A, how may I help you today? <-")
    speak("hello i am eva, how may i help you today")


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("evamachine94@gmail.com", "E.V.A.machine@69")
    server.sendmail("evamachine94@gmail.com", to, content)
    server.close()


def reminder(title, message):

    plyer.notification.notify(
        title=title,
        message=message,
        app_icon="assets\evalogo.ico",
        timeout=None
    )


if __name__ == "__main__":

    print("<-------------------------------------------------------------------------------------------------------------------------->")
    print("                                                           E.V.A                                                            ")
    print("<-------------------------------------------------------------------------------------------------------------------------->")

    wishMe()

    while True:
        query = takeCommand().lower()

        # logic for executing task based on query

        # ----------------------------------------------------------------------------------search queries

        if "wikipedia" in query:
            print("E.V.A: Searching Wikipedia.../ <-")
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia:")
            speak("according to wikipedia")
            print(results)
            speak(results)

        # -----------------------------------------------------------------------------------open queries

        elif "open google" in query:
            speak("opening google")
            print("E.V.A: Opening Google.../ <-")
            webbrowser.open("google.com")

        elif "open youtube" in query:
            speak("opening youtube")
            print("E.V.A: Opening Youtube.../ <-")
            webbrowser.open("youtube.com")

        elif "open stackoverflow" in query:
            speak("opening stackoverflow")
            print("E.V.A: Opening Stackoverflow.../ <-")
            webbrowser.open("stackoverflow.com")

        elif "open wikipedia" in query:
            speak("opening wikipedia")
            print("E.V.A: Opening Wikipedia.../ <-")
            webbrowser.open("wikipedia.com")

        elif "open instagram" in query:
            speak("opening instagram")
            print("E.V.A: Opening Instagram.../ <-")
            webbrowser.open("instagram.com")

        elif "open twitter" in query:
            speak("opening twitter")
            print("E.V.A: Opening Twitter.../ <-")
            webbrowser.open("twitter.com")

        elif "open whatsapp" in query:
            speak("opening whatsapp")
            print("E.V.A: Opening WhatsApp.../ <-")
            webbrowser.open("whatsapp.com")

        elif "open facebook" in query:
            speak("opening facebook")
            print("E.V.A: Opening Facebook.../ <-")
            webbrowser.open("facebook.com")

        elif "open" in query:
            query = query.replace("open", "")
            query = query.replace(" ", "")
            speak(f"opening {query}")
            print(f"E.V.A: Opening{query}.../ <-")
            try:
                webbrowser.open(f"{query}.com")
            except Exception as e:
                speak("sorry could not get that, can you please repeat")

        # -----------------------------------------------------------------------------------task queries

        elif "play music" in query:
            print("E.V.A: Which music shall i play? <-")
            speak("what music shall i play")
            query = takeCommand().lower()
            driver = webdriver.Chrome()
            driver.get(f"https://www.youtube.com/results?search_query={query}")
            song = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a")))
            song.click()

        # elif "stop music" in query:
        #     driver.close()

        elif "open visual studio" in query:
            codePath = "C:\\Users\\Meet\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "send email" in query:
            try:
                speak("please enter reciepents email address")
                to = input("E.V.A: Please enter the address:")
                print("E.V.A: What should i write? <-")
                speak("what should i write")
                content = takeCommand().lower()
                sendEmail(to, content)
                print("E.V.A: Email has been sent! <-")
                speak("email has been sent")
            except Exception as e:
                print("E.V.A: Sorry, not able to send the email, please try again! <-")
                speak("sorry, not able to send the email, please try again")

        # --------------------------------------------------------------------------------------------tell me queries

        elif "joke" in query:
            joke = pyjokes.get_joke(language="en", category="all")
            print(f"Eva: Here is one, {joke} <-")
            speak(f"here is one, {joke}")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"E.V.A: The time is {strTime} <-")
            speak(f"the time is {strTime}")

        elif "news" in query:
            # Init
            newsapi = NewsApiClient(api_key='dc60827e1a6140978812a8aec5504293')

            # /v2/top-headlines
            top_headlines = newsapi.get_top_headlines(
                language='en', country='in')

            print("E.V.A: Here are some latest news headlines <-")
            speak("here are some latest news headlines")
            for news in top_headlines["articles"]:
                title = news["title"]
                print(title)
                speak(title)

            # /v2/everything
            # all_articles = newsapi.get_everything(q='bitcoin',
            #                                     sources='bbc-news,the-verge',
            #                                     domains='bbc.co.uk,techcrunch.com',
            #                                     from_param='2017-12-01',
            #                                     to='2017-12-12',
            #                                     language='en',
            #                                     sort_by='relevancy',
            #                                     page=2)

            # all_articles = newsapi.get_everything(sources='bbc-news,the-verge',
            #                                       domains='bbc.co.uk,techcrunch.com',
            #                                       from_param='2021-01-01',
            #                                       to='2021-01-12',
            #                                       language='en',
            #                                       sort_by='relevancy',
            #                                       page=2)

            # /v2/sources
            sources = newsapi.get_sources()
            # print(top_headlines)
            # general q&a's

        elif "weather" in query:
            # importing requests and json
            # base URL
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
            speak("can you tell me your city")
            city = takeCommand().lower()
            CITY = city
            API_KEY = "0bf38d2b96e61d5bad3139a0b8f5f6f6"
            # upadting the URL
            URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
            # HTTP request
            response = requests.get(URL)
            # checking the status code of the request
            if response.status_code == 200:
                # getting data in the json format
                data = response.json()
                # getting the main dict block
                main = data['main']
                # getting temperature
                temperature = main['temp']
                # getting the humidity
                humidity = main['humidity']
                # getting the pressure
                pressure = main['pressure']
                # weather report
                report = data['weather']
                print(f"{CITY:-^30}")
                print(f"Temperature: {temperature-273.15}")
                print(f"Humidity: {humidity}")
                print(f"Pressure: {pressure}")
                print(f"Weather Report: {report[0]['description']}")
                description = data["weather"]
                description = data["main"]
                speak(
                    f"temperature is {round(temperature-273.15)} degree celcius")
                speak(
                    f"humidity in your city is {humidity} percent")
                speak(f"pressure in your city is {pressure} pascal")
                speak(f"the weather in your city is {report[0]['main']}")

            else:
                # showing the error message
                print("Error in the HTTP request")

        elif "quote" in query or "quotes" in query:
            # print("E.V.A: Quote of the day is:.../ <-")
            # speak("quote of the day is")
            # quote = wikiquote.quote_of_the_day()
            # print(quote)
            # speak(quote)
            print("E.V.A: Which personality's quote would you like to hear? <-")
            speak("which personality's quote would you like to hear")
            # personality = takeCommand().lower()
            quote = wikiquote.quotes(page_title="Bill Gates", max_quotes=1)
            print(quote)
            speak(quote)

        elif "reminder" in query:

            print("E.V.A: Ok, what should be the title of the reminder? <-")
            speak("ok, what should be the title of the reminder")

            title = takeCommand().lower()

            print("E.V.A: Ok, and what message should I add? <-")
            speak("ok, and what message should I add")

            message = takeCommand().lower()

            print(
                f"E.V.A: Got it, when do you wanna get reminded for {title}? <-")
            speak(f"got it, when do you wanna get reminded for {title}")

            # time = takeCommand().lower()
            # time = datetime.datetime.strptime(time, "%H:%M:%S")
            time = int(input("enter time: "))

            schedule.every(time).seconds.do(reminder, title, message)
            schedule.run_pending()

            # --------------------------------------------------------------------------os_commamds

        elif "empty recycle bin" in query:
            print("E.V.A: Are you sure you want me to empty recycle bin? <-")
            speak("are you sure you want me to empty recycle bin")
            input = takeCommand().lower()
            if input == "no":
                print("E.V.A: Ok, aborting the process <-")
                speak("ok, aborting the process")
            else:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                print("E.V.A: Recycle bin is emptied! <-")
                speak("recycle bin is emptied")

        elif "battery" in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            plugged = "Plugged In" if plugged else "Not Plugged In"
            print(percent+'% | '+plugged)
            speak(f"the battery percentage is {percent}, the battery is curretly {plugged}")
            if int(percent) <= 15 and plugged != "Plugged In":
                print("E.V.A: Please charge the system <-")
                speak("please charge the system")

        elif "system specifications" in query:
            print("E.V.A: Here are the system specifications <-")
            speak("Here are the system specifications")
            print(platform.processor())
            speak(f"the processor is {platform.processor()}")
            print(platform.version())
            speak(f"the version is {platform.version()}")
            print(platform.platform())
            speak(f"the platform is {platform.platform()}")
            print(platform.machine())
            speak(f"the machine is {platform.machine()}")
            print(platform.system())
            speak(f"the system is {platform.system()}")

        elif "brightness" in query:
            print("E.V.A: What percent of brightness should i set it at? <-")
            speak("What percent of brightness should i set it at")
            percent = takeCommand().lower()
            percent = re.findall("\d+", percent)
            percent = percent[0]
            percent = int(percent)
            sbc.set_brightness(percent)
            print(f"E.V.A: Changed the brightness to {percent} percent <-")
            speak(f"changed the brightness to {percent} percent")

            




#
