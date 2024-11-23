def char_count(text: str) -> dict[str, int]:
    chars_counts = {}
    for char in text.lower():
        if char.isalpha():
            chars_counts[char] = chars_counts.get(char, 0) + 1
    return dict(sorted(chars_counts.items(), key=lambda x: x[0]))

def word_count(text: str) -> int:
    return len(text.split())

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    wordcount = word_count(file_contents)
    chars_counts = char_count(file_contents)
    print(f"### Report on {book_path} ###")
    print(f"{wordcount} words found in the book")
    for k, v in chars_counts.items():
        print(f"The '{k}' character was found {v} times")
    print("### End of the report ###")

if __name__ == "__main__":
    main()
