def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lowered_text = text.lower()
    num_words = get_num_words(text)
    chars = list(lowered_text)
    character_count = count_chars(chars)
    listdic_of_dic = dic_to_listdic(character_count)
    sorted_dic = dic_sort(listdic_of_dic)
    print_report(book_path, num_words, sorted_dic)  


def dic_to_listdic(dic):
    dic_list = []
    for char,count in dic.items():
        new_dic = {"char": char, "num": count}
        dic_list.append(new_dic)
    return dic_list

def sort_on(dic):
    return dic["num"]

def dic_sort(dic):
    return sorted(dic, reverse=True, key=sort_on)

def print_report(path, word_count, sorted_listdic):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    
    for char_dict in sorted_listdic:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
        
    print("--- End report ---")



def count_chars(chars):
    char_count = {}
    for char in chars:
        if char.isalpha():
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