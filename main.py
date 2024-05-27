def main():
    book_path = "books/frankenstein.txt"
    raw_text = get_book(book_path)
    num_words = count_words(raw_text)
    print(f"{num_words} words found in the document")
    dictionary(raw_text)
    

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
    
def dictionary(text):
    lowered_string = text.lower()
    letters = []
    for letter in lowered_string:
        letters.append(letter)
    letter_counts = dict(dict.fromkeys(letters))
    for name in letter_counts:
        
        letter_counts[0] = count_letters(text, name)
    print(letter_counts)

main()