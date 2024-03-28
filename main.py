def get_num_words(input_text):
    return len(input_text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(input_text):
    letters_dict = {}

    for letter in input_text:
        letter = letter.lower()

        if letter not in letters_dict:
            letters_dict[letter] = 0
        else:
            letters_dict[letter] = letters_dict[letter] + 1

    return letters_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_dict = get_letter_count(text)
    print(num_words)
    print(letters_dict)


main()