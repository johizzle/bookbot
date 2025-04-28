def get_book_text(book_path):
    # returns the content of file as a string
    with open(book_path) as f:
        return f.read()

def number_of_words(book_string):
    return len(book_string.split())

def main():
    words = number_of_words(get_book_text("books/frankenstein.txt"))
    print(f"{words} words found in the document")


main()