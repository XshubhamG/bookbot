def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    sorted_char_dict = get_sorted_char_dict(chars_dict)
    print_report(sorted_char_dict, path, num_words)


# get book text
def get_book_text(path):
    with open(path) as f:
        return f.read()


# count words in string
def get_num_words(str):
    word_list = str.split()
    return len(word_list)


# chararcter sorted list
def get_sorted_char_dict(chars_dict):
    return dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))


# get the character dict
def get_char_dict(text):
    char_list = list(text.lower())
    char_dict = {}

    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


# print report
def print_report(sorted_dict, path, num_words):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words in the document\n")

    for char in sorted_dict:
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {sorted_dict[char]} times")

    print("--- End report ---")


main()
