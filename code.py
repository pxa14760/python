#!/usr/bin/env python3.5
''' This Script allows to take two input files and print to output the lines numbers from file2 
	where the name in file1 is found 
'''
file1 = 'names.txt'   #names.txt and details.txt files are in same directory where script is running
file2 = 'details.txt'   

list1 = [x.strip() for x in open(file1,'r').readlines()]
#print(list1)
list2 = [x.strip() for x in open(file2,'r').readlines()]
#print(list2)

for line in list1:
	#print(line)
	numbers = [item+1 for item in range(len(list2)) if line in list2[item]]
	myString = ",".join(map(str,numbers))
	print(line+':'+myString)
