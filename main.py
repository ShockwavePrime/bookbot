def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    print("Number of words:", num_words)
    report = book_report(text, num_words, book_path)
    print(report)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
        

def number_of_words(text):
    words = text.split()
    return len(words)
    


def sort_on(dict):
    return dict["number"]

def book_report(text, num_words, book_path):
    def character_count(text):
        # only contain letters from the alphabet and lowercase
        lowered_text = ''.join(c.lower() for c in text if c.isalpha())
        # c.isalpha() checks if c is an alphabetic character
        return {x : lowered_text.count(x) for x in set(lowered_text)}

    # Create the list of dictionaries for each character's occurences
    char_count = character_count(text)
    new_list = [{"character": x, "number": count} for x, count in char_count.items()]
   
   #Sort the list by the number of occurences
    new_list.sort(reverse=True, key=sort_on)

   #Report generation
    print(f"--- Begin report of {book_path}---")
    print(f"{num_words} words found in the document.")
    print(f"")
    for item in new_list:
        print(f"The {item['character']} character was found {item['number']} times!")
    print("--- End report ---")

    
main()


