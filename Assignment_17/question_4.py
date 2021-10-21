class HangmanWord:
    def __init__(self, word) -> None:
        self.word = word.lower()
        self.guessed_letters = []
    
    def __str__(self) -> str:
        revealed_word = []

        for letter in self.word:
            if letter in self.guessed_letters:
                revealed_word.append(letter)
            else:
                revealed_word.append("_")

        return ' '.join(revealed_word)

    def char_in_word(self, char):
        char = char.lower()
        return char in self.word

    def reveal_letter(self, char):
        char.lower()
        self.guessed_letters.append(char)

    def _validate_character(self, char):
        char.lower()
        if(len(char) and char.isalpha()):
            return self.char_in_word(char)

hangword = HangmanWord("Testing")
print(hangword)
print(hangword.char_in_word("I"))
print(hangword.char_in_word("A"))
hangword.reveal_letter("t")
print(hangword)
hangword.reveal_letter("e")
hangword.reveal_letter("s")
print(hangword)
hangword.reveal_letter("i")
hangword.reveal_letter("n")
hangword.reveal_letter("g")
print(hangword)