import re
import string

alpha_chars = re.compile(r"[a-zA-Z]")
punc_chars = re.compile(f"[{re.escape(string.punctuation)}]")


def count_words(book_text):
    return len(book_text.split())


def count_chars(text, char_regex):
    chars = [str.lower(char) for char in list(text)]

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


def sort_char_count(char_count_dict):
    sorted_chars_dict = sorted(
        char_count_dict.items(), key=lambda item: item[1], reverse=True
    )
    return [{"char": item[0], "count": item[1]} for item in sorted_chars_dict]
