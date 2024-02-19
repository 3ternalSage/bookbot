def word_count(text):
    return len(text.split())

def get_all_text_from_file(f):
    return f.read()

def get_letter_count(text):
    letters = {}
    for char in text:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def print_report(file_name, word_count, letter_count):
    print(f"--- Report of {file_name} ---")
    print(f"{word_count} words were found in this document.")
    print(f"")
    for l in letter_count:
        if not l[0].isalpha():
            continue
        print(f"The character '{l[0]}' was found {l[1]} times.")
    print(f"--- End of Report ---")

def main():
    book_file_name = "books/frankenstein.txt"
    with open(book_file_name) as f:
        text = get_all_text_from_file(f)
        wc = word_count(text)
        letter_count = get_letter_count(text.lower())
        letter_count = sorted(list(letter_count.items()), key=lambda x: x[1], reverse=True)
        print_report(book_file_name, wc, letter_count)


if __name__ == "__main__":
    main()