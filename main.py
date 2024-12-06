def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def number_of_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    print("Number of words:", word_count)

def character_count(file_contents):
    output = {x : file_contents.count(x) for x in set(file_contents)}
    print("Character count for each character is:\n"+ str(output))

main()

