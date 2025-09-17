def get_num_words(str):
    return len(str.split())


def get_char_freq(str: str):
    chars = list(str.lower())
    char_freq = {}
    for char in chars:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq


def get_sorted_char_freq(char_freq):
    return dict(sorted(char_freq.items(), key=lambda item: item[1], reverse=True))


def print_report(sorted_char_freq, path, num_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, freq in sorted_char_freq.items():
        if char.isalpha():
            print(f"{char}: {freq}")
