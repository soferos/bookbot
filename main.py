def main():
    book_path = "books/frankenstein.txt"
    raw_text = get_book(book_path)
    num_words = count_words(raw_text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    count_and_report(raw_text)
    print("--- End Report ---")
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text, key):
    global count
    lowered_string = text.lower()
    letters = []
    for letter in lowered_string:
        if letter in key:
            letters.append(letter)
            count = len(letters)
        return count

def get_book(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def count_and_report(text):
    lowered_string = text.lower()
    letter_dict = {letter:0 for letter in lowered_string if letter.isalpha()}
    for letter in text:
        if letter in letter_dict:
            letter_dict[letter] += 1
    dict_list = [{key: value} for key, value in letter_dict.items()]
    dict_list.sort(reverse=True, key=sort_on)
    for item in dict_list:
        key = list(item.keys())[0]
        value = list(item.values())[0]
        if key.isalpha():
            print(f"The '{key}' character was found {value} times.")
        else:
            return None

def sort_on(d):
    return list(d.values())[0]


main()