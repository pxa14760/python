#!/usr/bin/env python3.5
file1 = "names.txt"
file2 = "details.txt"
def line_number(phrase,filename):
	value = phrase.rstrip()
	d = dict()
	d.setdefault(value,[])
	with open(filename, 'r') as g:
		for linenum, line in enumerate(g, 1):
			if value in line:
				d[value].append(linenum)
	print(d)

def main_func():
	f = open(file1)
	for item in f:
		line_number(item, file2)

main_func()
