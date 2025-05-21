import re
import string

alpha_chars = re.compile(r'[a-zA-Z]')
punc_chars = re.compile(f'[{re.escape(string.punctuation)}]')

def count_words(book_text):
    return len(book_text.split())


def count_chars(text, char_regex):
    chars = list(text)
    chars = list(map(str.lower, chars))

    char_count = {}
    for char in chars:
        if char in char_count and re.match(char_regex, char):
            char_count[char] += 1
        elif re.match(char_regex, char):
            char_count[char] = 1

    return char_count


def count_alpha_chars(text):
    return count_chars(text, alpha_chars)

def count_punc_chars(text):
    return count_chars(text, punc_chars)
