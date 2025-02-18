def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lowered_text = text.lower()
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    chars = list(lowered_text)
    print (len(chars))
    character_count = count_chars(chars)
    print (character_count)

def count_chars(chars):
    char_count = {}
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()