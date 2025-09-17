from stats import get_char_freq, get_num_words, get_sorted_char_freq, print_report
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_freq = get_char_freq(text)
    sorted_char_freq = get_sorted_char_freq(char_freq)
    print_report(sorted_char_freq, path, num_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
