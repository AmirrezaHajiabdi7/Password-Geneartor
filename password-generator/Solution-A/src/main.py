import random
import string
from abc import ABC, abstractmethod
from typing import List, Optional

import nltk
from nltk.corpus import words


nltk.download('words', quiet=True)


class PasswordGeneration(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass


class PinGeneration(PasswordGeneration):
    def __init__(self, length: int = 4):
        self.length = length

    def generate(self) -> str:
        return ''.join(random.choice(string.digits) for _ in range(self.length))


class RandomPasswordGeneration(PasswordGeneration):
    def __init__(self, length: int = 16, include_numbers: bool = False, include_punctuation: bool = False):
        self.length = length
        self.characters: str = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_punctuation:
            self.characters += string.punctuation

    def generate(self) -> str:
        return ''.join(random.choice(self.characters) for _ in range(self.length))


class MemorablePasswordGeneration(PasswordGeneration):
    def __init__(
            self,
            num_of_words: int = 4,
            separator: str = '_',
            capitalize: bool = False,
            vocabulary: Optional[List[str]] = None
    ):
        if vocabulary is None:
            vocabulary = words.words()

        self.num_of_words: int = num_of_words
        self.capitalize: bool = capitalize
        self.separator: str = separator
        self.vocabulary: List[str] = vocabulary

    def generate(self) -> str:
        pass_words = [random.choice(self.vocabulary)
                      for _ in range(self.num_of_words)]
        if self.capitalize:
            pass_words = [
                word.upper() if random.choice([True, False]) else word.lower()
                for word in pass_words
            ]
        return self.separator.join(pass_words)


if __name__ == "__main__":
    print("PIN:", PinGeneration().generate())
    print("Random Password:", RandomPasswordGeneration(
        include_numbers=True, include_punctuation=True).generate())
    print("Memorable Password:", MemorablePasswordGeneration(
        capitalize=True).generate())
