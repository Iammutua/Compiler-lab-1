import re
import sys

def tokenize_sentence(sentence):
    # We will use regular expressions to identify the words
    # The word begins with a word boundary followed by zero or many word characters and ends with another boundary character
    words = re.findall(r'\b\w+\b', sentence)
    
    # printing each word
    for word in words:
        print(word)

# Input sentence (Here we prefer to pick it from the terminal using arguments passed to the program)
input_sentence = sys.argv[1]

# Tokenize the sentence and print the individual words
tokenize_sentence(input_sentence)
