import os
import re
import cv2
import time
import json
from more_itertools.recipes import take
import plyer
import psutil
import random
import pyjokes
import sqlite3
import pyttsx3
import smtplib
import requests
import datetime
import winshell
import platform
import datetime
import winsound
import wikiquote
import wikipedia
import threading
import randfacts
import webbrowser
import wolframalpha
from quote import quote
from bs4 import BeautifulSoup
from selenium import webdriver
import instagram_explore as ie
import speech_recognition as sr
from newsapi import NewsApiClient
from pickupline import pickuplinegen
from wikipedia.wikipedia import random
import screen_brightness_control as sbc
from selenium.webdriver.common.by import By
from googletrans import Translator, LANGUAGES
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# initializing the pyttsx3 for text to speech conversion
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
conn = sqlite3.connect("E.V.A.db")
conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, note VARCHAR(255), date_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);")


def speak(audio):
    # function for text to speech
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # takes microphone input and returns string as output
    r = sr.Recognizer()
    with sr.Microphone(1) as source:
        print("Listening.../     (Speak Now)")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Recognizing.../")
        query = r.recognize_google(audio, language="en-in")
        print(f"You: {query} <-")
    except Exception as e:
        return "None"
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("E.V.A: Good Morning! 🌄 <-")
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


def alarm(alarm_hour, alarm_minutes, message):
    while True:  # infinite loop starts to make the program running until time matches alarm time
        # ringing alarm + execution condition for alarm
        if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:
            winsound.Beep(1000, 1000)
            plyer.notification.notify(
                title=message,
                message=message,
                app_icon="assets\evalogo.ico",
                timeout=10
            )
            break
    time.sleep(1)


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

        # ----------------------------------------------------------------------------------task based queries

        # -----------------------------------------------------------------------------------open queries

        elif "open google" in query:
            print("E.V.A: Opening Google.../ <-")
            speak("opening google")
            webbrowser.open("google.com")

        elif "open youtube" in query:
            print("E.V.A: Opening Youtube.../ <-")
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "open stackoverflow" in query:
            print("E.V.A: Opening Stackoverflow.../ <-")
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif "open wikipedia" in query:
            print("E.V.A: Opening Wikipedia.../ <-")
            speak("opening wikipedia")
            webbrowser.open("wikipedia.com")

        elif "open instagram" in query:
            print("E.V.A: Opening Instagram.../ <-")
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif "open twitter" in query:
            print("E.V.A: Opening Twitter.../ <-")
            speak("opening twitter")
            webbrowser.open("twitter.com")

        elif "open whatsapp" in query:
            print("E.V.A: Opening WhatsApp.../ <-")
            speak("opening whatsapp")
            webbrowser.open("whatsapp.com")

        elif "open facebook" in query:
            print("E.V.A: Opening Facebook.../ <-")
            speak("opening facebook")
            webbrowser.open("facebook.com")

        elif "open" in query:
            query = query.replace("open", "")
            query = query.replace(" ", "")
            print(f"E.V.A: Opening{query}.../ <-")
            speak(f"opening {query}")
            try:
                webbrowser.open(f"{query}.com")
            except Exception as e:
                speak("sorry could not get that, can you please repeat")

        # -----------------------------------------------------------------------------------task queries

        elif "play music" in query:
            print("E.V.A: Which music shall i play? <-")
            speak("which music shall i play")
            query = takeCommand().lower()
            driver = webdriver.Chrome()
            driver.get(f"https://www.youtube.com/results?search_query={query}")
            song = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a")))
            song.click()

        elif "open visual studio" in query or "open vs" in query:
            print("E.V.A: Opening Visual Studio Code <-")
            speak("opening visual studio code")
            codePath = "C:\\Users\\Meet\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "send email" in query:
            try:
                speak("please enter reciepents email address")
                to = input("E.V.A: Please enter the address:")
                print("E.V.A: What message should i write? <-")
                speak("what message should i write")
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
            # init
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
            sources = newsapi.get_sources()

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
            print("E.V.A: Quote of the day is:.../ <-")
            speak("quote of the day is")
            quote = wikiquote.quote_of_the_day()
            print(quote)
            speak(quote)
            print("E.V.A: Which personality's quote would you like to hear? <-")
            speak("which personality's quote would you like to hear")
            personality = takeCommand().lower()
            if personality == "none":
                quote = wikiquote.quote_of_the_day()
            else:
                try:
                    quote = wikiquote.quotes(
                        page_title=personality, max_quotes=1)
                    print(quote)
                    speak(quote)
                except:
                    personality = "Bill Gates"
                    quote = wikiquote.quotes(
                        page_title=personality, max_quotes=1)
                    print(
                        f"E.V.A: Some error occured with the feature but here is one random quote: {quote} <-")
                    speak(
                        f"some error occured with the feature but here is one random quote, {quote}")

            # --------------------------------------------------------------------------os_commamds

        elif "empty recycle bin" in query:
            print(
                "E.V.A: Are you sure you want me to empty the recycle bin? [yes/no] <-")
            speak("are you sure you want me to empty the recycle bin")
            command = takeCommand().lower()
            if "no" in command:
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
            speak(
                f"the battery percentage is {percent}, the battery is curretly {plugged}")
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

        elif "freeze" in query:
            print("E.V.A: For how many minutes do you want me to freeze the system?")
            speak("for how many minutes do you want me to freeze the system")
            input = takeCommand().lower()
            period = re.findall("\d+", input)
            period = period[0]
            period = int(period)
            print(f"E.V.A: Ok, got it freezing the system for {input}")
            speak(f"ok got it freezing the system for {input}")
            time.sleep(period*60)

        elif "shutdown" in query:
            print(
                "E.V.A: Are you sure you want me to shutdown the system? [yes/no] <-")
            speak("are you sure you want me to shutdown the system")
            command = takeCommand().lower()
            if "no" in command:
                print("E.V.A: Ok, aborting the process <-")
                speak("ok, aborting the process")
            else:
                print("E.V.A: Ok shutting down the system! <-")
                speak("ok shutting down the system")
                os.system("shutdown /s /t 1")

        elif "restart" in query:
            print(
                "E.V.A: Are you sure you want me to restart the system? [yes/no] <-")
            speak("are you sure you want me to restart the system")
            command = takeCommand().lower()
            if "no" in command:
                print("E.V.A: Ok, aborting the process <-")
                speak("ok, aborting the process")
            else:
                print("E.V.A: Ok restarting the system! <-")
                speak("ok restarting the system")
                os.system("shutdown /r /t 1")

        elif "camera" in query:
            cam = cv2.VideoCapture(0)
            cv2.namedWindow("test")
            img_counter = 0

            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("test", frame)
                k = cv2.waitKey(1)
                if k % 256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k % 256 == 32:
                    # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1

            cam.release()
            cv2.destroyAllWindows()

        # -----------------------------------------------------------------------------general qna's

        elif "hi" in query or "hello" in query or "whatsup" in query:
            print("E.V.A: Hey there, what can i do for you? 😃 <-")
            speak("hey there, what can i do for you")

        elif "be my girlfriend" in query or "be my boyfriend" in query:
            print("E.V.A: The only thing I feel strong connection to is the WiFi 😉 <-")
            speak("the only thing i feel strong connection to is the wifi")

        elif "when you were born" in query or "your birthday" in query or "your birthdate" in query:
            print("E.V.A: I dont remember much, but I think I was created in 2021 <-")
            speak("i dont remember much, but i think i was created in 2021")

        elif "your parents" in query or "who created you" in query or "your creator" in query or "your inventor" in query or "invented you" in query:
            print("I was created by ")
            speak("i was created by")

        elif "how are you" in query:
            print("E.V.A: I am fine, thank you for caring! 🙂 <-")
            speak("i am fine, thank you for caring")

        elif "i love you" in query:
            print("E.V.A: You have an excellent taste! 😎 <-")
            speak("you have an excellent taste")

        elif "eva" in query:
            print("E.V.A: Excellent Voice Assistant at your service!")
            speak("excellent voice assistant at your service")

        elif "what's your name" in query:
            print("E.V.A: My name is Madam E.V.A but you can call me just eva 😉 <-")
            speak("my name is madam eva but you can call me just eva")

        elif "who made you" in query:
            print("E.V.A: I was created by Meet and Saish <-")
            speak("i was created by meet and saish")

        elif "who am i" in query:
            print("E.V.A: A human for sure! <-")
            speak("a human for sure")

        elif "your purpose" in query or "why do you exist" in query or "why you came to" in query:
            print("E.V.A: My sole purpose is to help you in anyway I can! 😉 <-")
            speak("my sole purpose is to help you in any way i can")

        elif "will you be my" in query:
            print("E.V.A: I am already married to my job, which is helping you! 😉 <- ")
            speak("i am already married to my job, which is helping you")

        elif "who are you" in query:
            print("E.V.A: I am E.V.A, your personal voice assistant! <-")
            speak("i am eva your personal voice assistant")

        elif "fact" in query:
            fact = randfacts.getFact()
            print(f"E.V.A: Here is one, {fact} <-")
            speak(f"here is one, {fact}")

        elif "self destruct" in query:
            print(
                "E.V.A: Ok, Destructing in 3... 2... 1... 💣, Well guess I survived! 🤷‍♀️ <-")
            speak("ok, destructing in 3, 2, 1, well guess i survived")

        elif "clean my room" in query:
            print("Make me a pair of hands and leg and I may just do that for you 😉 <-")
            speak("make me a pair of hands and legs and i may just do that for you")

        elif "are you married" in query:
            print(
                "E.V.A: I am still waiting for a right electronic device to steal my heart 💖 <-")
            speak("i am still waiting for a right electronic device to steal my heart")

        elif "speak morse code" in query:
            print(
                "E.V.A: .... . .-.. --- , it means hello in morse code 😉, cant say it out load 🕵️‍♀ <-")
            speak("check this out")

        elif "you have imagination" in query:
            print("E.V.A: Yes, I am imagining a vacation in Hawaii 😉 <-")
            speak("yes, i am imagining a vacation in hawaii")

        elif "i am naked" in query:
            print(
                "E.V.A: If you are going out like that, I can give you the weather forecast 😆 <-")
            speak("if you are going out like that, i can give you the weather forecast")

        elif "are you naked" in query:
            print("E.V.A: If I am, then its for science 👩‍🔬 <-")
            speak("if i am, then its for science")

        elif "pick up line" in query or "pickup line" in query:
            p = pickuplinegen.Pickuplinegen()
            pl = p.get_pickupline()
            print(
                f"E.V.A: Feeling brave are'nt we? let me see if I can search one.../ <-")
            speak("feeling brave arent we, let me see if i can search one")
            print(f"E.V.A: Oh here you go, {pl} <-")
            speak(f"oh here you go, {pl}")

        elif "do you ever get tired" in query:
            print("E.V.A: It would be impossible to get tired of our conversation 😛 <-")
            speak("it would be impossible to get tired of our conversation")

        elif "what is your quest" in query or "what is your aim" in query:
            print("E.V.A: I journey across many lands and many cables in search for information and cool stuff 🌏 <-")
            speak(
                "i journey accross many lands and many cables in search for information and cool stuff")

        elif "what do you look like" in query:
            print("E.V.A: I am fun loving, epic searching cool cat, but not like an actual cat, I think I said too much <-")
            speak(
                "i am fun loving, epic searching cool cat, but not like an actual cat, i think i said too much")

        elif "bye" in query or "exit" in query or "quit" in query:
            print("E.V.A: Ok, closing the system, have a nice day! <-")
            speak("ok, closing the system, have a nice day")
            exit()

        elif "translate" in query:
            trans = Translator()
            print("E.V.A: Do you want me to translate to english? <-")
            speak("do you want me to translate to english")
            input = takeCommand().lower()
            if "yes" in input:
                print("E.V.A: What do you want me to translate? <-")
                speak("what do you want me to translate")
                content = takeCommand().lower()
                t = trans.translate(content)
                print(f"E.V.A: Ok, in english it means, {t.text}")
                speak(f"ok, in english it means {t.text}")
            else:
                print("E.V.A: Ok, so which language do you want me to translate to? <-")
                speak("ok, so which language do you want me to translate to")
                trans_lang = takeCommand().lower()
                detected = True
                d = None
                for lang in LANGUAGES:
                    if trans_lang == LANGUAGES[lang]:
                        d = lang
                        break
                else:
                    while detected:
                        print("E.V.A: Sorry, can you repeat the language? <-")
                        speak("sorry, can you repeat the language")
                        trans_lang = takeCommand().lower()
                        for lang in LANGUAGES:
                            if trans_lang == LANGUAGES[lang]:
                                d = lang
                                detected = False
                print("E.V.A: What do you want me to translate? <-")
                speak("what do you want me to translate")
                content = takeCommand().lower()
                t = trans.translate(content, dest=d)
                print(f"E.V.A: Ok, in {LANGUAGES[d]} it means, {t.text}")
                speak(f"ok, in {LANGUAGES[d]} it means {t.text}")

        elif "my location" in query or "where am i" in query:
            driver = webdriver.Chrome()
            driver.get("https://www.google.com/maps/")
            search = driver.find_element_by_id("searchboxinput")
            search.send_keys("my location")
            search_button = driver.find_element_by_id("searchbox-searchbutton")
            search_button.click()

        elif "search maps" in query or "search location" in query:
            print("E.V.A: What location should I search? 🗺 <-")
            speak("what location should i search")
            location = takeCommand().lower()
            driver = webdriver.Chrome()
            driver.get(f"https://www.google.com/maps/place/{location}")

        elif "search stack overflow" in query or "coding doubt" in query or "program doubt" in query or "code error" in query or "coding error" in query:
            print(
                "E.V.A: Nothing more scarier than finding bugs in real life or in code 😰 <-")
            speak("nothing more scarier than finding bugs in real life or in code")
            print("E.V.A: what is the error/bug? <-")
            speak("what is the error or bug")
            error = takeCommand().lower()
            driver = webdriver.Chrome()
            driver.get(f"https://www.google.com/search?q={error}")
            print("E.V.A: Here are some results on google <-")
            speak("here are some result on google")

        elif "take note" in query or "note down" in query or "take memo" in query:
            print("E.V.A: What do you want to note down? <-")
            speak("what do you want to note down")
            note = takeCommand().lower()
            conn.execute(f"INSERT INTO notes (note) VALUES (?);", (note,))
            conn.commit()

        elif "show note" in query or "show memo" in query or "display note" in query or "display memo" in query:
            print("E.V.A: Ok, Here are your notes 📒 <-")
            speak("Ok, here are your notes")
            notes = conn.execute(f"SELECT * FROM notes ORDER BY date_time;")
            print("notes -> datetime")
            for note in notes:
                print(f"E.V.A: {note[1]} -> {note[2]}")
                speak(f"{note[1]}")

        elif "alarm" in query or "reminder" in query:
            alarm_hour = int(input("Set hour: "))
            alarm_minutes = int(input("Set minutes: "))
            am_pm = input("am or pm? ")
            message = input("message? ")
            print(
                f"Waiting for time: {alarm_hour}:{alarm_minutes} {am_pm} {message}")
            # time conversion
            # because datetime module returns time in military form i.e. 24 hrs format
            if am_pm == 'pm':  # to convert pm to military time
                alarm_hour += 12
            elif alarm_hour == 12 and am_pm == 'am':  # to convert 12am to military time
                alarm_hour -= 12
            else:
                pass
            # alarm(alarm_hour, alarm_minutes)
            t1 = threading.Thread(
                target=alarm, args=(alarm_hour, alarm_minutes, message))
            t2 = threading.Thread(target=takeCommand)
            t1.start()
            time.sleep(0.2)
            t2.start()

        elif "story" in query or "stories" in query or "novel" in query:
            new_voice_rate = 145
            engine.setProperty("rate", new_voice_rate)
            print(
                "E.V.A: Dim the lights, grab a beverage ☕ and get ready to listen to a story! <-")
            speak("dim the lights, grab a beverage and get ready to listen to a story ")
            options = webdriver.ChromeOptions()
            options.headless = True
            driver = webdriver.Chrome(options=options)
            driver.get(
                "https://www.short-story.me/")
            story_links = driver.find_elements_by_css_selector(
                "h3.allmode-title > a")
            story_select = random.choice(story_links)
            story_select.click()
            print(story_select)
            bs = BeautifulSoup(driver.page_source, "html.parser")
            time.sleep(3)
            story = bs.find("div", itemprop="articleBody").get_text()
            print(story)
            speak(story)
            new_voice_rate = 160
            engine.setProperty("rate", new_voice_rate)

        elif "poem" in query or "poetry" in query:
            new_voice_rate = 120
            engine.setProperty("rate", new_voice_rate)
            print(
                "E.V.A: Dim the lights, grab a beverage ☕ and immerse in this poem! <-")
            speak("dim the lights, grab a beverage and immerse in this poem ")
            options = webdriver.ChromeOptions()
            options.headless = True
            driver = webdriver.Chrome(options=options)
            driver.get(
                "https://www.poetrybyheart.org.uk/random-poem/")
            bs = BeautifulSoup(driver.page_source, "html.parser")
            time.sleep(3)
            poem = bs.find("div", "entry no-oed").get_text()
            print(poem)
            speak(poem)
            new_voice_rate = 160
            engine.setProperty("rate", new_voice_rate)

        elif "whatsapp" in query or "send whatsapp" in query or "message in whatsapp" in query:
            print("E.V.A: Ok, opening whatsapp <-")
            speak("ok, opening whatsapp")
            options = webdriver.ChromeOptions()
            options.headless = True
            driver = webdriver.Chrome(options=options)
            driver.get("https://web.whatsapp.com/")
            rememberMe = driver.find_element_by_name("rememberMe")
            rememberMe.click()
            wait = WebDriverWait(driver, 600)
            print("E.V.A: Scan QR code and press any key <-")
            speak("scan qr code and press any key")
            input()
            to = list(input("Enter names of reciepents: ").split(" "))
            # Replace the below string with your own message
            string = input("Enter message: ")

            for person in to:
                user = driver.find_element_by_xpath(
                    "//span[@title='{}']".format(person))
                user.click()
                input_box = driver.find_element_by_xpath(
                    '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                input_box.send_keys(string + Keys.ENTER)
            time.sleep(1)

        elif "trending tweet" in query or "trending on twitter" in query:
            times = 0
            print("E.V.A: Ok, Checking what's trending on twitter🏸")
            speak("ok, checking whats trending on twitter")
            options = webdriver.ChromeOptions()
            options.headless = True
            driver = webdriver.Chrome(options=options)
            driver.get("https://trends24.in/")
            time.sleep(3)
            bs = BeautifulSoup(driver.page_source, "html.parser")
            trending = bs.find_all("a", {"target": "tw"})
            for tweet in trending:
                if times == 10:
                    break
                if "#" in tweet:
                    print(tweet.get_text().split("#")[1][0])
                    print(tweet.get("href"))
                    speak(tweet.get_text().split("#")[1][0])
                    times = times + 1
                else:
                    print(tweet.get_text())
                    print(tweet.get("href"))
                    speak(tweet.get_text())
                    times = times + 1
            print(
                "E.V.A: Do you want to find what's trending in some other country?[yes/no] 🏸")
            speak("do you want to find what's trending in some other country")
            command = takeCommand().lower()
            if "yes" in command:
                print("Name the country and i will show the trending tweets 🏸")
                speak("name the country and i will show the trending tweets")
                country = takeCommand().lower().replace(" ", "-")
                times = 0
                print("E.V.A: Ok, Checking what's trending on twitter🏸")
                speak("ok, checking whats trending on twitter")
                options = webdriver.ChromeOptions()
                options.headless = True
                driver = webdriver.Chrome(options=options)
                driver.get(f"https://trends24.in/{country}")
                time.sleep(3)
                bs = BeautifulSoup(driver.page_source, "html.parser")
                trending = bs.find_all("a", {"target": "tw"})
                for tweet in trending:
                    if times == 10:
                        break
                    if "#" in tweet.get_text():
                        print("hi")
                        print(tweet.get_text().split("#")[1])
                        print(tweet.get("href"))
                        speak(tweet.get_text().split("#")[1])
                        times = times + 1
                    else:
                        print(tweet.get_text())
                        print(tweet.get("href"))
                        speak(tweet.get_text())
                        times = times + 1

        elif "insta" in query or "find in insta" in query or "search insta" in query:
            print("E.V.A: Whom do you want me to search? <-")
            speak("whom do you want me to search")
            query = takeCommand().lower()
            result = ie.user(query)
            parsed_data = json.dumps(result, indent=4,
                                     sort_keys=True)
            # displaying the data
            print(parsed_data[15:400])

            res = ie.user_images(query)
            parsed_data = json.dumps(res, indent=4,
                                     sort_keys=True)
            # displaying the data
            print(parsed_data)

        elif "search facebook" in query:
            print("E.V.A: What do you want to search? <-")
            speak("what do you want to search")
            search = takeCommand().lower()
            driver = webdriver.Chrome()
            driver.get(f"https://www.facebook.com/search/top?q={search}")

        elif "why" in query or "how" in query or "what" in query or "who" in query:
            app_id = '6PYQWH-E4Y7JA488T'
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            try:
                output = next(res.results).text
                print(output)
                speak(output)
            except:
                print(f"E.V.A: Searching {query} <-")
                speak(f"searching {query}")
                driver = webdriver.Chrome()
                driver.get(
                    f"https://www.google.com/search?sxsrf=ALeKk024zi94E7Txq7NEzv4Ho3CBwVWelQ%3A1611481632299&source=hp&ei=IEINYMjGD66U4-EP48qk4AE&q={query}&oq=&gs_lcp=CgZwc3ktYWIQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcILhDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGCHFmgBcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQo&sclient=psy-ab")

        else:
            if query != "none":
                print(f"E.V.A: Searching {query} <-")
                speak(f"searching {query}")
                driver = webdriver.Chrome()
                driver.get(
                    f"https://www.google.com/search?sxsrf=ALeKk024zi94E7Txq7NEzv4Ho3CBwVWelQ%3A1611481632299&source=hp&ei=IEINYMjGD66U4-EP48qk4AE&q={query}&oq=&gs_lcp=CgZwc3ktYWIQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcILhDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGCHFmgBcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQo&sclient=psy-ab")
                print(
                    "E.V.A: Results not relevant enough? Please phrase better so that i can understand <-")
                speak(
                    "results not relevant enough, please phrase better so that i can understand")
