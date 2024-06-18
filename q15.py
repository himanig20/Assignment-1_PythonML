'''Write a program that reads data from a CSV file and prints it to the
console.'''

import csv


with open('exampleq15.csv', mode = 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(', '.join(row))





