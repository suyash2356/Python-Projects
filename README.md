# Python Practice Projects

This repository contains small Python projects that I built to practice my programming skills and showcase my learning journey toward becoming a Data Scientist. These projects cover basic concepts such as file handling, automation, and user interaction.

## 📌 Projects

### 1️) Task Manager
A simple task manager that allows users to add, update, delete, and mark tasks as completed.
**Features:**
- Add and manage tasks easily.
- Store tasks in a structured format.
- View completed and pending tasks.
 

### 2️) Menu-Driven Calculator
A command-line calculator for performing basic mathematical operations.
**Features:**
- Supports addition, subtraction, multiplication, and division.
- Simple menu-driven interface.
 
 
 ### 3) Number Guessing Game
A game in which user have to guess the number from 1 to 100.
**Features:**
- Code display, how user answer is away or close to correct answer after each guessing.
- After final guessing of correct number,the number of attempt required is diplay.

   
### 4)AI Chatbot using OpenAI API
This is a chatbot built using Python and the OpenAI API, which allows users to have interactive conversations 
with an AI model. The chatbot takes user input, sends it to OpenAI’s API, and returns AI-generated responses.
**How It Works:**
Install the required package:
>pip install openai
**Get the OpenAI API Key:**
Create an account on OpenAI and generate an API key.
Store the API key securely in your script or use environment variables.
**Implement the Chatbot**
Import the OpenAI module and configure the API key.
Take user input and send it to the OpenAI API using openai.ChatCompletion.create().
Retrieve the AI-generated response and display it in a conversational format.
**Handle Errors and Optimization**
Implement error handling for API request failures.
Use efficient models like "gpt-3.5-turbo" for faster responses.
Ensure proper input validation and user-friendly interactions.
**How to Build Your Own**
Install Python and the OpenAI library.
Get an API key from OpenAI and integrate it into your script.
Use openai.ChatCompletion.create() to interact with the AI model.
Run the script in a loop to allow continuous conversation.
For more details, refer to OpenAI API Documentation.



### 5) Jarvis — A Voice-Controlled AI Assistant in Python
Jarvis is a voice-activated personal assistant built using Python, integrating real-time speech recognition, system automation, and AI-powered responses via OpenAI’s GPT API.

This project was created as a learning journey, exploring how various tools and APIs can be combined to build a real-world assistant — much like the fictional "Jarvis" from Iron Man. It uses libraries like vosk, pyttsx3, openai, and sounddevice, with extensive help from online documentation and AI tools like ChatGPT.

📌 Features
- 🎙️ Wake-word detection and continuous speech recognition
- 💬 Conversational AI via OpenAI (GPT-3.5)
- 📝 Reminders (save and recall anytime)
- 🌐 Webpage summarization
- 📁 Open system apps (Notepad, Calculator, Camera, etc.)
- 💻 Shutdown, Restart, and Sleep commands
- 🔗 Smart browser automation (Google, YouTube, LinkedIn, GitHub...)

**🔧 How I Built It**
This project was built inside a virtual environment in VS Code. I learned and implemented the tools using:
- Official library documentation
- Example code snippets from vosk, openai, etc.
- Tutorials and forums
- Occasional help from ChatGPT when stuck or exploring ideas
The idea wasn't to reinvent the wheel, but to build something real by stitching together resources, and this is exactly what this assistant represents.

**🛠️ Setup Instructions**
To run this project locally, follow these steps:

1. Clone the repo
```sh
git clone https://github.com/your-username/jarvis-assistant.git
cd jarvis-assistant
```
2. Set up a virtual environment

**Create a virtual environment (Windows)**
```sh
python -m venv venv
```

**Activate it**
```sh
venv\Scripts\activate
```
3. **Install dependencies**
```sh
pip install -r requirements.txt
```
(Note: Make sure you have vosk-model-small-en-us-0.15 or a similar Vosk model in the /model directory)

4. **Add your OpenAI API key**
Open the script and replace:

```sh
openai.api_key = "your-api-key-here"
```
with your actual API key from https://platform.openai.com/

5. **Run the assistant**
```sh
python jarvis.py
```
🎙️ How to Use
Say "Jarvis" to wake the assistant, then issue a command like:
- "Open Google"
- "Set reminder to call mom"
- "What are my reminders?"
- "Summarize https://some-news-site.com/article"
- "Shutdown"
- "Ask what is the capital of France?"
The assistant listens for a wake word before accepting commands. If the wake word isn't detected, it keeps listening passively.



## 📂 How to Use
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/suyash2356/Python-Projects.git
   ```
2. **Navigate to the Project Directory:**
   ```sh
   cd Python-Projects
   ```
3. **Run the Python Script:**
   ```sh
   python Project_name.py
   ```

## 🚀 Future Learning Goals
- Learn data analysis and visualization libraries.
- Work on real-world datasets.
- Build machine learning models.

## 📬 Contact
Feel free to connect with me on Linkedin:https://www.linkedin.com/in/suyash-anil-babad-ab367a30b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

