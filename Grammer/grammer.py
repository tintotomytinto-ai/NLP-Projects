import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

text = input("Enter a sentence: ")

matches = tool.check(text)

print("\nCorrected Sentence:")
print(tool.correct(text))

print("Grammar Mistakes Found:", len(matches))
