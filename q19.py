'''Write a python program that removes all punctuation from a given string.'''

import string

a = input("Enter string: ")

a = a.translate(str.maketrans('', '', string.punctuation))
print(a)

