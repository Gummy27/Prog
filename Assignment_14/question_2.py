import string

def main():
    a_sent = input("Enter in a sentence: ")
    b_sent = input("Enter in another sentence: ")

    a_sent_dict = string_to_dict(a_sent)
    b_sent_dict = string_to_dict(b_sent)

    if(compare_dicts(a_sent_dict, b_sent_dict)):
        print(f"{a_sent} is an anagram of {b_sent}.")
    else:
        print(f"{a_sent} is not an anagram of {b_sent}.")


# Write your functions here
def string_to_dict(sent):
    my_dict = {}
    sent = sent.lower()

    for letter in sent:
        if(letter not in string.punctuation):
            try:
                my_dict[letter] += 1
            except:
                my_dict[letter] = 1
    return my_dict

def compare_dicts(a_dict, b_dict):
    for letter in a_dict:
        try:
            if(a_dict[letter] != b_dict[letter]):
                return False
        except KeyError:
            return False
            
    return True
    
# Main functionality starts here
if __name__ == "__main__":
    main()