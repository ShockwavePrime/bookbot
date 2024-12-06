def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    print("Number of words:", num_words)
    char_count = character_count(text)
    print("Character count for each character is:\n"+ str(char_count))


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
        

def number_of_words(text):
    words = text.split()
    return len(words)
    

def character_count(text):
    lowered_text = text.lower()
    return {x : lowered_text.count(x) for x in set(lowered_text)}
    
main()


