'''Write a python program that checks if a substring is present in a given
string.'''

a = input("Enter string:")
sub_str = input("Enter substring:")

if sub_str in a:
    print("Substring is present")
else:
    print("Substring not present")