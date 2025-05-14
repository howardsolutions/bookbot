from stats import get_book_text, print_book_report

def main():
    book_contents = get_book_text('./books/frankenstein.txt')

    sorted_chars = print_book_report(book_contents)

main()