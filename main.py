import sys
from stats import get_word_count, get_book_text, chars_dict_to_sorted_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def print_report(book_path, word_count, sorted_list_of_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for chars in sorted_list_of_chars:
        if chars[0].isalpha():
            print(f"{chars[0]}: {chars[1]}")

    print("============= END ===============")


def main():
    word_count = get_word_count(sys.argv[1])
    char_count = get_book_text(sys.argv[1])
    sorted_list = chars_dict_to_sorted_list(char_count)
    print_report(sys.argv[1], word_count, sorted_list)
    
main()

