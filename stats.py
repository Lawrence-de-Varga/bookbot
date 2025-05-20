def count_words(book_text):
    return len(book_text.split())

def count_characters(text):
    chars = list(text)
    chars = list(map(str.lower, chars))

    char_count = {}
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
