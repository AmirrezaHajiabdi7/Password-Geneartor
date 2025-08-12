import random 
import string 
from typing import List, Optional
import nltk


def pin_password(length:int = 8) :
    return ''.join([random.choice(string.digits) for _ in range (length)])




def random_password (lenght:int = 12 , include_number:bool = False , include_symbol:bool = False) :

    rand_pass = string.ascii_letters
    if include_number :
        rand_pass+=string.digits

    if include_symbol :
        rand_pass+=string.punctuation
    
    return ''.join([random.choice(rand_pass) for _ in range(lenght)])

my_pass = random_password(include_number=True , include_symbol=True)



def memorable_password (
        num_of_word : int = 4 , 
        capitalize:bool =  False ,
        separator :str = '_',
        vocabulary:Optional[List[str]] = None 
):

    if vocabulary is None :
        vocabulary = nltk.corpus.words.words()
        
    Pass_Word = [random.choice(vocabulary) for _ in range (num_of_word)]

    if capitalize :
        Pass_Word = [word.upper() if random.choice([True , False]) else word.lower() for word in Pass_Word]

    return separator .join(Pass_Word)