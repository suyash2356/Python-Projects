import os
import sys
import queue
import webbrowser
import pyttsx3
import sounddevice as sd
import vosk
import json
import openai
import datetime
import difflib
import subprocess
import requests
from bs4 import BeautifulSoup

# =============== Text-to-Speech Setup ===============
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Optional: set male voice
voices = engine.getProperty('voices')
for voice in voices:
    if "male" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# =============== Load Vosk Model with Grammar ===============
model_path = "model"
if not os.path.exists(model_path):
    print("Vosk model not found in 'model/' folder.")
    sys.exit()

limited_phrases = json.dumps([
    "jarvis", "open google", "open youtube", "open linkedin", "open github",
    "open movies for you", "open kaggle", "stop", "ok bye", "set reminder",
    "what are my reminders", "my reminders", "ask", "question", "shutdown",
    "restart", "sleep", "summarize", "open notepad", "open calculator", "open camera"
])

model = vosk.Model(model_path)
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# =============== Speech Recognition ===============
def listen_command():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000, limited_phrases)
        print("Listening...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print("You said:", text)
                    return text

# =============== OpenAI Chat ===============
openai.api_key = "your-api-key-here"

def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return "Sorry, I couldn't reach OpenAI right now."

# =============== Reminder Functions ===============
REMINDER_FILE = "reminders.txt"

def save_reminder(text):
    with open(REMINDER_FILE, "a") as f:
        f.write(text + "\n")
    speak("Reminder saved.")

def read_reminders():
    if not os.path.exists(REMINDER_FILE):
        speak("You have no reminders.")
        return
    with open(REMINDER_FILE, "r") as f:
        reminders = f.readlines()
    if reminders:
        speak("Here are your reminders:")
        for r in reminders:
            speak(r.strip())
    else:
        speak("You have no reminders.")

# =============== Webpage Summarizer ===============
def summarize_webpage(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = " ".join(p.get_text() for p in paragraphs[:5])
        if not content.strip():
            speak("Couldn't read any content.")
            return
        summary = ask_openai("Summarize this:\n" + content)
        speak(summary)
    except Exception:
        speak("Failed to summarize the webpage.")

# =============== System Control ===============
def control_system(command):
    if "shutdown" in command:
        speak("Shutting down.")
        os.system("shutdown /s /t 1")
    elif "restart" in command:
        speak("Restarting.")
        os.system("shutdown /r /t 1")
    elif "sleep" in command:
        speak("Going to sleep.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# =============== Launch Apps ===============
def open_app(command):
    if "notepad" in command:
        subprocess.Popen(["notepad.exe"])
        speak("Opening Notepad.")
    elif "calculator" in command:
        subprocess.Popen(["calc.exe"])
        speak("Opening Calculator.")
    elif "camera" in command:
        subprocess.Popen("start microsoft.windows.camera:", shell=True)
        speak("Opening Camera.")
    else:
        speak("I can't open that app yet.")

# =============== Command Handler ===============
def processCommand(c):
    c = c.lower()
    print(f"Command: {c}")

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open github" in c:
        webbrowser.open("https://github.com")
    elif "open movies for you" in c:
        webbrowser.open("https://movies4u.mov/")
    elif "open kaggle" in c:
        webbrowser.open("https://www.kaggle.com/")
    elif "ask" in c or "question" in c:
        prompt = c.replace("ask", "").replace("question", "").strip()
        if prompt:
            response = ask_openai(prompt)
            speak(response)
        else:
            speak("Please tell me your question.")
    elif "set reminder" in c:
        reminder_text = c.replace("set reminder", "").strip()
        if reminder_text:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            save_reminder(f"{timestamp} - {reminder_text}")
        else:
            speak("Please tell me what to remind you about.")
    elif "my reminders" in c or "what are my reminders" in c:
        read_reminders()
    elif "summarize" in c and "http" in c:
        summarize_webpage(c.split("summarize", 1)[-1].strip())
    elif any(word in c for word in ["shutdown", "restart", "sleep"]):
        control_system(c)
    elif "open" in c:
        open_app(c)
    elif "ok bye" in c or "exit" in c:
        speak("Shutting down. Goodbye!")
        sys.exit()
    else:
        speak("I did not understand that command.")

# =============== Main Loop ===============
if __name__ == "__main__":
    speak("Initializing Jarvis. Ready when you are.")
    while True:
        command = listen_command()
        words = command.split()
        matches = difflib.get_close_matches("jarvis", words, cutoff=0.7)
        if matches:
            speak("Yes Sir.")
            command = listen_command()
            if command:
                processCommand(command)
        else:
            print("Wake word not detected.")
