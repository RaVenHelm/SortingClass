from SortingClass import *
from argparse import ArgumentParser
from copy import copy

import sys

a = [3, 1, 4, 1, 5, 9, 2, 6]


def main(arguments):
	SortingUtilClass.print_title(4, 'Quick Sort')
	s = SortingClass()
	func = arguments.algorithm
	if func == 'bubble':
		array = copy(a)
		s.bubble_sort(array)
	elif func == 'insertion':
		array = copy(a)
		s.insertion_sort(array)
	elif func == 'selection':
		array = copy(a)
		s.selection_sort(array)
	elif func == 'all':
		array = copy(a)
		s.all(array)
	else:
		print('Invalid algorithm')
		sys.exit(1)

if __name__ == '__main__':
	parser = ArgumentParser(description='Tester for Assignment #4')
	parser.add_argument('--algorithm', metavar='algorithm', default='all')
	parser.add_argument('--array', metavar='E', type=int, nargs='+')
	args = parser.parse_args()
	if args.array:
		a = args.array
	main(args)
