#!/usr/bin/env python3.5
file1 = 'names.txt'
file2 = 'details.txt'

list1 = [x.strip() for x in open(file1,'r').readlines()]
list2 = [x.strip() for x in open(file2,'r').readlines()]

for line in list2:
	numbers = [item+1 for item in range(len(list1)) if list1[item] == line]
	myString = ",".join(map(str,numbers))
	print(line+':'+myString)
