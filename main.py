from stats import get_num_words, get_each_character, sort_on, sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1];

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    text = get_book_text(path)
    num_words = get_num_words(text);
    each_word_dict = get_each_character(text);
    sorted_dict = sorted_list(each_word_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words");
    print("--------- Character Count -------")
    # print(each_word_dict);
    for item in sorted_dict:
        if item["name"].isalpha():
            name = item["name"]
            num = item["num"]
            print(f"{name}: {num}")

   



main()

