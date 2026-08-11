from spellchecker import SpellChecker
import language_tool_python
from deep_translator import GoogleTranslator


# -----------------------
# Language Configuration
# -----------------------

languages = {
    "1": ("English", "en", "en-US"),
    "2": ("Spanish", "es", "es"),
    "3": ("French", "fr", "fr"),
    "4": ("German", "de", "de-DE"),
    "5": ("Portuguese", "pt", "pt"),
    "6": ("Italian", "it", "it"),
    "7": ("Malayalam", "ml", None),
    "8": ("Hindi", "hi", None),
    "9": ("Arabic", "ar", "ar"),
}


print("========== NLP Language Tool ==========\n")


# -----------------------
# Input Language
# -----------------------

print("Select Input Language")

for key, value in languages.items():
    print(f"{key}. {value[0]}")

source_choice = input("\nEnter choice: ")

if source_choice not in languages:
    print("Invalid language choice")
    exit()


source_name, source_code, grammar_code = languages[source_choice]


text = input(f"\nEnter {source_name} text: ")



# -----------------------
# Spell Checking
# -----------------------

spell_text = text


try:
    spell = SpellChecker(language=source_code)

    corrected_words = []

    for word in text.split():

        clean_word = word.strip(".,!?")

        if clean_word.isalpha():

            correction = spell.correction(clean_word)

            corrected_words.append(correction)

        else:
            corrected_words.append(word)


    spell_text = " ".join(corrected_words)


except Exception:
    print("\nSpell checking not available for this language.")



print("\nSpell Corrected:")
print(spell_text)



# -----------------------
# Grammar Checking
# -----------------------

grammar_text = spell_text


if grammar_code:

    try:

        tool = language_tool_python.LanguageTool(grammar_code)

        matches = tool.check(spell_text)

        grammar_text = language_tool_python.utils.correct(
            spell_text,
            matches
        )


    except Exception as e:
        print("Grammar checking unavailable")



# Extra Grammar Rules

grammar_rules = {

    "How are you are": "How are you?",
    "how are you are": "How are you?",
    "how is you": "How are you?",
    "How is you": "How are you?",

    "I is": "I am",
    "you is": "you are",
    "You is": "You are",

    "He are": "He is",
    "She are": "She is",

    "They is": "They are",
    "We is": "We are",

    "I has": "I have",
    "He have": "He has",
    "She have": "She has"
}


for wrong, correct in grammar_rules.items():

    grammar_text = grammar_text.replace(
        wrong,
        correct
    )


# First letter capital
if grammar_text:
    grammar_text = grammar_text[0].upper() + grammar_text[1:]


print("\nGrammar Corrected:")
print(grammar_text)



# -----------------------
# Translation
# -----------------------

print("\nSelect Translation Language")

for key, value in languages.items():
    print(f"{key}. {value[0]}")


target_choice = input("\nEnter choice: ")


if target_choice not in languages:
    print("Invalid language choice")
    exit()



target_name, target_code, _ = languages[target_choice]


try:

    translated = GoogleTranslator(
        source="auto",
        target=target_code
    ).translate(grammar_text)


    print("\n==============================")
    print("Translated Text")
    print("==============================")

    print(translated)


except Exception as e:

    print("Translation error:", e)