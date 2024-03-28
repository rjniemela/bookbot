def get_num_words(input_text):
    return len(input_text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(input_text):
    letters_dict = {}

    for letter in input_text:

        if letter.isalpha():
            letter = letter.lower()
            if letter not in letters_dict:
                letters_dict[letter] = 0
            else:
                letters_dict[letter] = letters_dict[letter] + 1

    return letters_dict

def print_report(book_path, word_count, letters): 
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for letter in letters:
        print(f"The '{letter["letter"]}' character was found {letter["count"]} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_dict = get_letter_count(text)
    sorted_letters = []
    
    for letter in letters_dict:
        sorted_letters.append({"letter": letter, "count": letters_dict[letter]})
    
    sorted_letters.sort(reverse=True, key=sort_on)
    
    print_report(book_path=book_path, word_count=num_words,letters=sorted_letters)


main()