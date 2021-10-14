import string
from typing import Counter

def main():
    filename = input("Name of file: ")
    file_object = open(filename)
    word_list = get_word_list(file_object) 
    file_object.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuples(word_count_dict)
    print(sorted(word_count_tuples))
    avg_count_of_words(word_count_tuples)
    
def get_word_list(file_object):
    split_list = []
    word_list = file_object.read().split("\n")
    for x in word_list:
        split_list += x.split(" ")

    new_list = []
    for index in range(len(split_list)):
        new_word = processed_word(split_list[index])
        if(new_word != ""):
            new_list.append(new_word)
    
    return new_list

def processed_word(word):
    try:
        word = word.lower()
        word.strip()
        while(word[-1] in string.punctuation):
            word = word[:-1]
        
        return word
    except:
        return ""

def word_list_to_counts(word_list):
    word_pairs_dict = {}

    for word in word_list:
        try:
            word_pairs_dict[word] += 1
        except KeyError:
            word_pairs_dict[word] = 1

    return word_pairs_dict

def dict_to_tuples(word_count_dict):
    word_count_list = []

    for key, value in word_count_dict.items():
        word_count_list.append((key, value))

    return word_count_list

def avg_count_of_words(word_count_list):
    count = len(word_count_list)
    sum_of_count = 0
    for x in range(count):
        sum_of_count += word_count_list[x][1]
    
    print(f"Each word appeared on average {round(sum_of_count/count, 2):.2f} times.")

if __name__ == "__main__":
    main()