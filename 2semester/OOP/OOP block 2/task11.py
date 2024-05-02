import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print("Буквы алфавита:", self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase)

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."


# Пример использования
eng_alphabet = EngAlphabet()
eng_alphabet.print()
print("Количество букв в алфавите:", eng_alphabet.letters_num())
print("Буква F относится к английскому алфавиту?",
      eng_alphabet.is_en_letter('F'))
print("Буква Щ относится к английскому алфавиту?",
      eng_alphabet.is_en_letter('Щ'))
print("Пример текста на английском языке:", EngAlphabet.example())
