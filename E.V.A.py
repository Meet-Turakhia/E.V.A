import os
import pyjokes
import pyttsx3
import smtplib
import datetime
import wikipedia
import webbrowser
from selenium import webdriver
import speech_recognition as sr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyaudio


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
    print("E.V.A: I am E.V.A, how may I help you today? <-")
    speak("hello i am eva, how may i help you today")


def sendEmail(to, content):
    server = smtplib.smtp("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("your email address", "your password")
    server.sendmail("your email address", to, content)
    server.close()


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
                print(f"{query}.com")
            except Exception as e:
                speak("sorry could not get that, can you respell")

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

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"E.V.A: The time is {strTime} <-")
            speak(f"the time is {strTime}")

        elif "open visual studio" in query:
            codePath = "C:\\Users\\Meet\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "send email" in query:
            try:
                print("E.V.A: On what email address should i send? <-")
                speak("on what email address should i send")
                to = takeCommand().lower()
                print("E.V.A: What should i write? <-")
                speak("what should i write")
                content = takeCommand().lower()
                sendEmail(to, content)
                print("E.V.A: Email has been sent! <-")
                speak("email has been sent")
            except Exception as e:
                print("E.V.A: Sorry, not able to send the email, please try again! <-")
                speak("sorry, not able to send the email, please try again")

        elif "joke" in query:
            joke = pyjokes.get_joke(language="en", category="all")
            print(f"Eva: Here is one, {joke} <-")
            speak(f"here is one, {joke}")

        # general q&a's
