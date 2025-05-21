from stats import count_words, count_alpha_chars, count_punc_chars

def get_book_text(book_path):
    with open(book_path) as b:
        contents = b.read()

    return contents

def main():
    franken = get_book_text("books/frankenstein.txt")
    word_count = count_words(franken)
    char_count = count_alpha_chars(franken)
    punc_count = count_punc_chars(franken)
    # print(f"{char_count} charactersfound in the document")
    print(char_count)
    print()
    print(punc_count)
main()    
