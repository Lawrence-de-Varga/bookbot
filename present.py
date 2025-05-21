def present_chars_and_counts(sorted_char_count_dict):
    [print(f"{entry['char']}: {entry['count']}") for entry in sorted_char_count_dict]


def present_book_stats(word_count, sorted_char_dict, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    present_chars_and_counts(sorted_char_dict)

    print("============= END ===============")
