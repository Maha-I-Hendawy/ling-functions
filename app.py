from functions import clean_words, find_prefix, find_suffix, find_pronoun
from text import Text, Person, Customer

text = input("Enter text here")

t = Text(text)

words = [w for w in text.split()]

sentences = [s for s in text.split('.')]


clean_words(words)

find_prefix(words)

find_suffix(words)

find_pronoun(words)





