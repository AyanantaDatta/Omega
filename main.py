import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey   # Replace with your OpenAI API key
    chatStr += f"Ayan: {query}\n Omega: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey  # Replace with your OpenAI API key
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):
    import win32com.client as wincl
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry!"

if __name__ == '__main__':
    print('Welcome to Omega')
    say("Hi I am Omega")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],["chatgpt", "https://chat.openai.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "open music" in query:
            musicPath = r"C:\Users\91980\Downloads\Best_of_Arijit_Singh.mp3"  # Replace with the correct path to the music file
            os.system(f"start {musicPath}")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} past {min} minutes")

        elif "open code" in query.lower():
            vs_code_path = r"C:\Users\91980\AppData\Local\Programs\Microsoft VS Code\Code.exe" # Replace with the correct path to the Code.exe
            os.system(f"start \"\" \"{vs_code_path}\"")

        elif "open spotify" in query.lower():
            os.system("start spotify")  # Replace with the correct path to any application

        elif "Using artificial intelligence" in query:
            ai(prompt=query)

        elif "Omega Quit" in query:
            exit()

        elif "reset chat" in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)


