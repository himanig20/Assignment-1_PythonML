'''Write a python program that generates the first n numbers in the
Fibonacci sequence.'''

n = int(input("Enter a number:"))
a = 0
b = 1
print ("Fibonacci sequence:")
for i in range(0, n):
    print(a)
    c = a + b
    a = b
    b = c
    i +=1

    
