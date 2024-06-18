#Write a python program that calculates the factorial of a given number.

a = int(input("Enter a number:"))
f = 1
for i in range(1,a+1):
    f = f*i

print("The factorial of the given number is:", f)