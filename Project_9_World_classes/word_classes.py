from os import read
import string

WORD_CLASSES = [
    "a",
    "c",
    "f",
    "l",
    "n",
    "s"
]

def main():
    original_word_list = read_file()
    print()
    
    if(original_word_list):
        print(original_word_list)
        print()

        no_punct_word_list = remove_punctuation(original_word_list)
        print(no_punct_word_list)
        print()

        all_word_dict, longest_word_dict = word_list_into_dict(no_punct_word_list)

        print_out_dict(all_word_dict)
        print()

        print_out_dict(longest_word_dict)
# Functions come here

def read_file() -> list:
    """
        This function will read the file and return it split into
        words.
    """ 
    filename = input("Enter file name: ")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()

            return two_split_delimiters(data, [" ", "\n"])
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return []
      
def print_out_dict(word_dict):
    for word_class in WORD_CLASSES:
        print(f"{word_class}:")
        
        last_word = ""
        for word in sorted(word_dict[word_class]):
            if(word != last_word):
                spacing = " "*(20-len(word))
                print(spacing+word)
                last_word = word

def two_split_delimiters(text: str, delimiters: list) -> list:
    """
        This function will take in a string and multiple delimiters
        and split them up into a list.
    """
    split_text = []
    prev_split = -1

    for text_index in range(len(text)):
        for delimiter in delimiters:
            if(text[text_index] == delimiter):
                split_text.append(text[prev_split+1:text_index])
                prev_split = text_index

    split_text.append(text[prev_split+1:text_index+1])

    return split_text

def word_list_into_dict(word_list: list) -> dict:
    """
        This functino takes in a word list and puts it into
        dictionary using the word classes as keys. It also
        finds the largest word in each group and puts it 
        into a dictionary
    """
    all_word_dict = {}
    longest_word_dict = {}
    
    for word_index in range(0, len(word_list), 2):
        word = word_list[word_index]
        word_class = word_list[word_index+1][0]
        try:
            all_word_dict[word_class].append(word)

            longest_word = longest_word_dict[word_class][0]

            if(len(longest_word) < len(word)):
                longest_word_dict[word_class][0] = word

            elif(len(longest_word) == len(word)):
                longest_word_dict[word_class][0] = sorted([longest_word, word])[0]
        except:
            all_word_dict[word_class] = [word]
            longest_word_dict[word_class] = [word]
    
    return all_word_dict, longest_word_dict


def remove_punctuation(text_list: list) -> list:
    """
        This function takes in a word list and removes
        the punctuations.
    """
    for text_index in range(len(text_list), 0, -1):
        if(text_list[text_index-1] in string.punctuation):
            text_list.pop(text_index-1)
    return text_list

# Main program starts here
if __name__ == "__main__":
    main()