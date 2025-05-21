import sys
from stats import count_words, count_alpha_chars
from stats import sort_char_count
from present import present_book_stats


def get_book_text(book_path):
    with open(book_path) as b:
        contents = b.read()

    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book = get_book_text(path)
    word_count = count_words(book)
    char_count = count_alpha_chars(book)

    sorted_chars = sort_char_count(char_count)
    present_book_stats(word_count, sorted_chars, path)


main()
