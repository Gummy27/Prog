# Keep these 2 lines
text_to_translate = input("Text to translate: ")
VOWELS = "aeiouyAEIOUY"

# ...add your code here

translation = ""
if(text_to_translate):
    for word in text_to_translate.split(" "):
        if(word[0] in VOWELS):
            translation += word+"yay "
        else:
            consonants_to_be_added = ""
            index_of_vowel = 0  

            # Will run until it finds the first vowel in the word.
            for letter_index in range(len(word)):
                if(word[letter_index] not in VOWELS):
                    consonants_to_be_added += word[letter_index]
                else:
                    index_of_vowel = letter_index
                    break
            
            translation += word[index_of_vowel:] + consonants_to_be_added + "ay "

# Keep this line
print("Translation:", translation)
