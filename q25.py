'''Write a program that copies the contents of one text file to another'''

with open('firstq25.txt','r') as firstfile, open('secondq25.txt','w') as secondfile: 
	
	for line in firstfile: 
	    secondfile.write(line)
		

