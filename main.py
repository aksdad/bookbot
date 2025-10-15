from typing import List
from stats import get_num_words, sorted_char_freq
import sys

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {file_path}...')
    contents = get_book_text(file_path)
    # print(contents)
    print("----------- Word Count ----------")
    num_words = get_num_words(contents)
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    sorted_char_freq(contents)
    for item in sorted_char_freq(contents):
        ch, count = item["char"], item["num"]
        if ch.isalpha():
            print(f'{ch}: {count}')
    print("============= END ===============")


main()
