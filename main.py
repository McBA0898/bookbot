import sys
from stats import count_words

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_counts = count_characters(text)
    print_report(book_path, num_words, character_counts)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_characters(text):
    text_lower = text.lower()
    character_counts = {}
    for char in text_lower:
        if char.isalpha():
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    return character_counts

def print_report(book_path, num_words, character_counts):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    sorted_characters = sorted(character_counts.items(), key=lambda item:item[1], reverse=True)
    for char, count in sorted_characters:
        print(f"{char}: {count}")
    print("--- End Report ---")


main()

