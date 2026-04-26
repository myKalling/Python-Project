
## Simple Text Cleaner & Analyzer
## This program lets you enter text, clean it up
## (lowercase, remove punctuation, strip spaces),
## and then run basic word stats — all through
## an easy menu you can loop through as much as you want.

 
import string

def capture_text():
    print("\nEnter your text (press Enter twice to finish):")
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
    if not text.strip():
        print("[no text entered]")
        return ""
    return text


def clean_text(text):
    # Strip whitespace
    stripped = text.strip()

    # Lowercase
    lowered = stripped.lower()

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleaned = lowered.translate(translator)

    return cleaned


def analyze_words(cleaned_text):
    words = cleaned_text.split()

    if not words:
        print("\nNo words to analyze.")
        return

    total_words = len(words)
    avg_length = sum(len(w) for w in words) / total_words

    print("\n--- Text Summary ---")
    print(f"Total words: {total_words}")
    print(f"Average word length: {avg_length:.2f}")


def menu():
    original_text = ""
    cleaned_text = ""

    while True:
        print("\n===== TEXT ANALYZER MENU =====")
        print("1. Enter new text")
        print("2. Clean & normalize text")
        print("3. Show cleaned text")
        print("4. Analyze word statistics")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            original_text = capture_text()
            cleaned_text = ""  # reset cleaned version

        elif choice == "2":
            if not original_text:
                print("No text entered yet.")
            else:
                cleaned_text = clean_text(original_text)
                print("\nCleaned text:")
                print(cleaned_text)

        elif choice == "3":
            if cleaned_text:
                print("\nCleaned text:")
                print(cleaned_text)
            else:
                print("You must clean the text first (option 2).")

        elif choice == "4":
            if cleaned_text:
                analyze_words(cleaned_text)
            else:
                print("You must clean the text first (option 2).")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    menu()
