# Capturing multiline input
print("Enter your text (press Enter twice to finish):")
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)
print("You entered:")
if text:
    print(text)
else:
    print("[no text entered]")

# .lower() lowercase option
lowercase_choice = input("\nConvert to lowercase? (yes/no): ").lower()
if lowercase_choice == "yes" or lowercase_choice == "y":
    normalized_text = text.lower()
    print(normalized_text)
else:
    print(text)
    
# Strip the whitespace from the beginning and end of the text
stripped_text = text.strip()
print("\nText after stripping whitespace:")
print(stripped_text)

s = "Hello, World! Python is amazing."

# Remove punctuation with string.punctuation
import string
translator = str.maketrans('', '', string.punctuation)

# Remove punctuation
clean_text = s.translate(translator)
print(clean_text)

### Add Menu loop for user to choose options