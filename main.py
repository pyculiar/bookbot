def char_count(text: str) -> dict[str, int]:
    text = text.lower()
    chars_counts = {}
    for char in text:
        if char.isalpha():
            if char not in chars_counts.keys():
                chars_counts[char] = 1
            else:
                chars_counts[char] += 1
    chars_counts = sorted(chars_counts.items(), key=lambda x: x[1], reverse=True)
    return dict(chars_counts)

def word_count(text: str) -> int:
    words = text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    print(f"### Report on {book_path} ###")
    with open(book_path) as f:
        file_contents = f.read()
    wordcount = word_count(file_contents)
    print(f"{wordcount} words found in the book")
    chars_counts = char_count(file_contents)
    for k, v in chars_counts.items():
        print(f"The '{k}' character was found {v} times")
    print("### End of the report ###")

if __name__ == "__main__":
    main()
