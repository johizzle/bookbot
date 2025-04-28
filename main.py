from stats import get_num_words

def get_book_text(book_path):
    # returns the content of file as a string
    with open(book_path) as f:
        return f.read()

def main():
    words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{words} words found in the document")


main()