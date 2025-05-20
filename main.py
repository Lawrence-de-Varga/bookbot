from stats import count_words, count_characters

def get_book_text(book_path):
    with open(book_path) as b:
        contents = b.read()

    return contents

def main():
    franken = get_book_text("books/frankenstein.txt")
    word_count = count_words(franken)
    char_count = count_characters(franken)
    # print(f"{char_count} charactersfound in the document")
    print(char_count)

main()    
