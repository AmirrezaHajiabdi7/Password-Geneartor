# Password Generation Library

A simple Python library for generating different types of passwords:
- Numeric PINs
- Random character-based passwords
- Memorable word-based passwords

This library is built with an **OOP design** using Python's `ABC` module for abstraction, making it easy to extend and customize.

---

## Features
1. **PinGeneration** – Generates numeric PIN codes of a given length.
2. **RandomPasswordGeneration** – Generates random passwords with letters, optional digits, and optional punctuation.
3. **MemorablePasswordGeneration** – Generates easy-to-remember passwords made of real words, with optional capitalization and custom separators.

---

## Requirements
- Python 3.8+
- [NLTK](https://www.nltk.org/) for word-based password generation.

Install dependencies:
```bash
pip install nltk
```

## For **MemorablePasswordGeneration**, download the NLTK word corpus:
```python
import nltk
nltk.download('words')
```

## Usage
``` python
from password_generator import PinGeneration, RandomPasswordGeneration, MemorablePasswordGeneration

# PIN
pin = PinGeneration(length=6).generate()
print("PIN:", pin)

# Random password with numbers and punctuation
random_pass = RandomPasswordGeneration(length=12, include_numbers=True, include_punctuation=True).generate()
print("Random Password:", random_pass)

# Memorable password
memorable_pass = MemorablePasswordGeneration(num_of_words=4, separator='-', capitalize=True).generate()
print("Memorable Password:", memorable_pass)
```

## Class Overview
> PasswordGeneration  

- Defines the abstract **generate()** method that all password types must implement.

> PinGeneration

- **Arguments:**
- **length** *(int)* – number of digits in the PIN (default: 4).
- Example Output: **4827**

> RandomPasswordGeneration
- **Arguments :**
- **length** (int) – password length (default: 16)

- **include_numbers** (bool) – include digits (default: False)

- **include_punctuation**(bool) – include special characters (default: False)

- Example Output: **Aq9$dkP@zL1mXv**

> MemorablePasswordGeneration

- **Arguments:**

 - **num_of_words** (int) – number of words in the password (default: 4)

- **separator** (str) – string used to join words (default: _)

- **capitalize** (bool) – randomly capitalize some words (default: False)

- **vocabulary** (List[str]) – custom list of words (optional)

- Example Output: **apple-DOG-sky-CAR**


## Notes

- **MemorablePasswordGeneration** uses the NLTK **words** corpus by default, which may not be available without downloading.

- You can pass your own vocabulary list to avoid using NLTK data.
