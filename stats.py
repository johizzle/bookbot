#functions that analyze the text
def get_num_words(book_string):
    return len(book_string.split())

def get_num_char(book_string):
    lower_string = book_string.lower()
    char_dict = {}
    for i in lower_string:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict

def sort_dict(char_dict):
    #Takes each pair in char_dict and adds to a list (of dictionaries)
    new_list = []
    for k, v in char_dict.items():
        new_list.append({"char": k, "num": v})    
    
    #Scoped private function for .sort() method below
    def sort_on(dict):
        return dict["num"]
    
    #Sorts the list (reversed) based on the key, which is a function object (without parentheses) that 
    # .sort() uses to sort by (return value)
    new_list.sort(reverse=True, key=sort_on)
    return new_list