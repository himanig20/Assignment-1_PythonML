'''Write a program in python that checks if a string starts with a given prefix
or ends with a given suffix.'''

def starts_with_prefix(string, prefix):
    return string.startswith(prefix)

def ends_with_suffix(string, suffix):
    return string.endswith(suffix)


string = input("Enter the string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")
    
if starts_with_prefix(string, prefix):
    print(f"The string starts with the prefix '{prefix}'.")
else:
    print(f"The string does not start with the prefix '{prefix}'.")

if ends_with_suffix(string, suffix):
    print(f"The string ends with the suffix '{suffix}'.")
else:
    print(f"The string does not end with the suffix '{suffix}'.")

