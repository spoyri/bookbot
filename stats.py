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