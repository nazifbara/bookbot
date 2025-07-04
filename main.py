from stats import get_num_words, get_chars_dict, sort_chars_dict

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_path = './books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_chars_dict(chars_dict)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_chars:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()

main()