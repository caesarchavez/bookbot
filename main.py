from stats import get_book_words
from stats import get_characters
def main(): 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = get_book_words(book_path)
    count_words = get_characters(book_path)
    print(f"Found {total_words} total words")
    print(count_words)
    
def get_book_text(path):
    with open(path) as f: 
        return f.read()
    
    
main()