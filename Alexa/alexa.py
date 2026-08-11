import webbrowser
from datetime import datetime
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

command = input("You: ").lower()

if command == "open google":
    response = "Opening Google"
    print("Alexa:", response)
    engine.say(response)
    engine.runAndWait()
    webbrowser.open("https://www.google.com")

elif command == "open youtube":
    response = "Opening YouTube"
    print("Alexa:", response)
    engine.say(response)
    engine.runAndWait()
    webbrowser.open("https://www.youtube.com")

elif command == "open github":
    response = "Opening GitHub"
    print("Alexa:", response)
    engine.say(response)
    engine.runAndWait()
    webbrowser.open("https://github.com")

elif command == "open gmail":
    response = "Opening Gmail"
    print("Alexa:", response)
    engine.say(response)
    engine.runAndWait()
    webbrowser.open("https://mail.google.com")

elif command == "open colab":
    response = "Opening Google Colab"
    print("Alexa:", response)
    engine.say(response)
    engine.runAndWait()
    webbrowser.open("https://colab.research.google.com")

elif command == "time now":
    current_time = datetime.now().strftime("%I:%M %p")
    response = f"The current time is {current_time}"
    print("Alexa:", response)
    engine.say(response)
    engine.runAndWait()

elif command == "date today":
    today = datetime.now().strftime("%d %B %Y")
    response = f"Today's date is {today}"
    print("Alexa:", response)
    engine.say(response)
    engine.runAndWait()

else:
    response = "Sorry, I don't understand."
    print("Alexa:", response)
    engine.say(response)
    engine.runAndWait()

    