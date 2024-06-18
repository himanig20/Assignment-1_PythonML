'''Write a program that reads the content of a text file and prints it to the
console.'''
file_path = "textq6.txt"
with open(file_path, "r") as file:
    file_content = file.read()

print("File content:\n", file_content)