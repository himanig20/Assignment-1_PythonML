'''Write a python program that calculates the sum of the digits of a given
number.'''

a = int(input("Enter a number:"))
sum = 0 
b = a
while(b>0):
    sum = sum + b%10
    b //= 10

print(sum)
