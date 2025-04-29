from stats import get_num_words, get_num_char, sort_dict

def get_book_text(book_path):
    # returns the content of file as a string
    with open(book_path) as f:
        return f.read()

def main():
    words = get_num_words(get_book_text("books/frankenstein.txt"))
    #returns a list with dictionaries with the key and value names char and num
    character_list = sort_dict(get_num_char(get_book_text("books/frankenstein.txt")))
    output = ""
    for entry in character_list:
        if entry['char'].isalpha():
            output += f"{entry['char']}: {entry['num']}\n"

    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------
{output}============= END ===============""")
    
main()