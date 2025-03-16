def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_each_character(text):
    letters_dict = {}
    
    for character in text.lower():
        if character in letters_dict:
            letters_dict[character] += 1;
        else:
            letters_dict[character] = 1;

    return letters_dict

def sort_on(dict):
    return dict["num"]


def sorted_list(dictionary):
    pairs = [];
    for name, num in dictionary.items():
        pairs.append({"name": name, "num": num})

    pairs.sort(reverse=True, key=sort_on)
    return pairs


