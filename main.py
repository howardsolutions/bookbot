from stats import count_words_in_book, get_book_text, count_characters

def main():
    book_contents = get_book_text('./books/frankenstein.txt')
    # count_words_in_book(book_contents)
    
    char_count = count_characters(book_contents)
    print("\nCharacter counts in the book:")
    print(char_count)

main()