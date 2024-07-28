def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lower_case_text = lower(text)
    num_words = get_num_words(text)
    letter_count = charcter_count(lower_case_text)
    print(f"{num_words} words found in the document\n")
    for letter, count in letter_count.items():
        print(f"The '{letter}' character was found '{count}' times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def lower(text):
    lower_case = text.lower()
    return lower_case

def charcter_count(lower_case_text):
    from collections import Counter, OrderedDict
    letters_only = ''.join(filter(str.isalpha, lower_case_text))
    letters = Counter(letters_only)
    ordered_letters = OrderedDict(letters.most_common())
    return ordered_letters

main()