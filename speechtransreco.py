import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

# Initialize
r = sr.Recognizer()
translator = Translator()

# Listen to speech
with sr.Microphone() as source:
    print(" Speak in English...")
    audio = r.listen(source)

try:
    # Speech to English text
    english = r.recognize_google(audio, language="en-US")
    print("\nEnglish:")
    print(english)

    # English to Malayalam
    malayalam = translator.translate(english, dest="ml").text
    print("\nMalayalam:")
    print(malayalam)

    # Malayalam speech
    tts = gTTS(text=malayalam, lang="ml")
    tts.save("malayalam.mp3")
    playsound("malayalam.mp3")

    print("Playing Malayalam audio...")
    playsound("malayalam.mp3")


except Exception as e:
    print("Error:", e)

    