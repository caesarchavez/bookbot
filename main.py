from stats import get_count_words, get_count_characters, get_sorted_list
import sys

def main(): 
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1) 
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_count_words(text)
    num_characters = get_count_characters(text)
    char_sorted_list = get_sorted_list(num_characters)
    print_report(book_path, num_words,num_characters, char_sorted_list)
    
              
        

def get_book_text(book_path): 
    with open(book_path) as f: 
        book_contents = f.read()
        
    return book_contents
        

def print_report(book_path, num_words, num_characters, char_sorted_list):
    print ("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
