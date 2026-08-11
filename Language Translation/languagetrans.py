from deep_translator import GoogleTranslator

languages = {
    "English": "en",
    "Malayalam": "ml",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Telugu": "te",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar"
}

print("Available Languages:")
for lang in languages:
    print("-", lang)

source = input("\nEnter source language: ").title()
target = input("Enter target language: ").title()

if source not in languages or target not in languages:
    print("Invalid language selected.")
    exit()

text = input("\nEnter text: ")

translated = GoogleTranslator(
    source=languages[source],
    target=languages[target]
).translate(text)

print("\nTranslated Text:")
print(translated)