import sys

from stats import get_book_contents, print_book_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path_to_book = sys.argv[1]
    book_contents = get_book_contents(path_to_book)

    sorted_chars = print_book_report(book_contents)

main()