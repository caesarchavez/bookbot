def get_count_words(text): 
    num_words = text.split()
    return len(num_words)

def get_count_characters(text): 
        chars ={}
        
        for c in text: 
            lowered = c.lower()
            if lowered in chars: 
                chars[lowered] += 1 
            else: 
                chars[lowered] = 1
        return chars
        
def sort_on(d):
    return d["num"]

def get_sorted_list(text_dict): 
    sorted_dict = [] 
    
    for ch in text_dict: 
        sorted_dict.append({"char": ch, "num": text_dict[ch]})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict