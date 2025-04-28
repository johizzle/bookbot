#functions that analyze the text
def get_num_words(book_string):
    return len(book_string.split())

def get_num_char(book_string):
    lower_string = book_string.lower()
    char_dict ={}
    for i in lower_string:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict
