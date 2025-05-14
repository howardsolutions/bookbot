def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_words_in_book(contents):
    list_of_words = contents.split()
    num_words = len(list_of_words)
    print(f"{num_words} words found in the document")

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
