from stats import get_num_words, get_num_char, sort_dict
import sys

def get_book_text(book_path):
    # returns the content of file as a string
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        #exit program with a status code of 1 using sys.exit(1)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    words = get_num_words(get_book_text(f"{book_path}"))
    #returns a list with dictionaries with the key and value names char and num
    character_list = sort_dict(get_num_char(get_book_text(f"{book_path}")))
    output = ""
    for entry in character_list:
        if entry['char'].isalpha():
            output += f"{entry['char']}: {entry['num']}\n"

    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------
{output}============= END ===============""")
    
main()