#!/usr/bin/env python3.5
file1 = 'names.txt'
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
