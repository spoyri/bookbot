import sys
from stats import word_count
from stats import unique_character_count
from sys import argv, exit

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    path = argv[1]
    with open(path) as f:
        file_contents = f.read()
        words = word_count(file_contents)
        chars = unique_character_count(file_contents)
        print("--- Begin report of " + path + " ---")
        print(f"{words} words found in the document")
        print()

        for i in chars:
            if not i.isalpha():
                continue
            print(f"{i}: {chars[i]}")
        
        print("--- End report ---")


main()