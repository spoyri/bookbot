def main():
    path = "books/frankenstein.txt"
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
            print(f"The '{i}' character was found {chars[i]} times")
        
        print("--- End report ---")

def word_count(book : str):
    return len(book.split())

def unique_character_count(book):
    chars = {}
    for i in book.lower():
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars


main()