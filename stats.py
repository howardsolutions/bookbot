def get_book_contents(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_words_in_book(contents):
    list_of_words = contents.split()
    num_words = len(list_of_words)
    return num_words

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():  # Only count alphabetical characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def print_book_report(book_contents):
    characters_dict = count_characters(book_contents)
    
    char_list = []
    
    for char, count in characters_dict.items():
        char_list.append({"char": char, "count": count})
    
    char_list.sort(reverse=True, key=lambda x: x["count"])
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words_in_book(book_contents)} total words")
    print("--------- Character Count -------")
    for char_dict in char_list:
        print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")
    
    return char_list
    