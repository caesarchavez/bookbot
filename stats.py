def get_book_words(path):
    with open(path) as f: 
        text = f.read()
        words = text.split()
        return len(words)

def get_characters(path): 
    with open(path) as f: 
        text = f.read()
        lowercase = text.lower()
        char = {}
        for letters in lowercase:
            if letters in char:
                char[letters] += 1
            else:
                char[letters] = 1
        return char 
            
        