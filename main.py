def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()
    
def count_words(text: str):
    words = text.split()
    return len(words)

def main():
    text = get_book_text('./books/frankenstein.txt')
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

main()