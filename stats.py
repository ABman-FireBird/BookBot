def get_word_count(path):
   
    with open(path) as f:
    
        file_contents = f.read()
        words = file_contents.split()
        print(f"Found {len(words)} total words")
        return len(words)



def get_book_text(path):
    
    word_dict = {}    
    with open(path) as f:
        
        file_contents = f.read()
        lower = file_contents.lower()
        
        for char in lower:
            if char not in word_dict:
                word_dict[char] = 1
            else:
                word_dict[char] += 1
    return word_dict

def sort_on(books: tuple[str, int]) -> int:
    return books[1]

def chars_dict_to_sorted_list(word_dict: dict[str, int]) -> list[tuple[str, int]]:
    new_list = []
    sorted_book = []
    for keys in word_dict.items():
        new_list.append(keys)
        
    sorted_book = sorted(new_list, key=sort_on, reverse=True)
    return sorted_book







