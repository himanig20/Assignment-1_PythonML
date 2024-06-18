'''Write a program that takes a string input from the user and writes it to a
text file'''
data = input("Enter something:")
a = open("textq5.txt", "w")
a.write(data)
