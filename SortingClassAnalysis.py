from SortingClass import *
from argparse import ArgumentParser
# from copy import copy
from random import sample
# from math import ceil

import sys

ANALYSIS_TIMES = 10
# LIST_SIZES = [10, 50, 100, 500, 1000]
LIST_SIZES = [10]

total_comparisons = {'bubble': 0, 'selection': 0, 'insertion': 0, 'qsort': 0, 'heap': 0}


def bubble(size):
	array = sample(range(size), size)
	s = SortingClass(to_print=False)
	analysis = s.bubble_sort(array).get_analysis()
	comparisons = analysis['comparisons']
	return comparisons


def selection(size):
	array = sample(range(size), size)
	s = SortingClass(to_print=False)
	analysis = s.selection_sort(array).get_analysis()
	comparisons = analysis['comparisons']
	return comparisons


def insertion(size):
	array = sample(range(size), size)
	s = SortingClass(to_print=False)
	analysis = s.insertion_sort(array).get_analysis()
	comparisons = analysis['comparisons']
	return comparisons


def qsort(size):
	array = sample(range(size), size)
	s = SortingClass(to_print=False)
	analysis = s.quick_sort(array, len(array), 0, len(array) - 1).get_analysis()
	comparisons = analysis['comparisons']
	return comparisons


def heap_sort(size):
	array = sample(range(size), size)
	s = SortingClass(to_print=False)
	analysis = s.heap_sort(array, len(array)).get_analysis()
	comparisons = analysis['comparisons']
	return comparisons

SORTS = [bubble, selection, insertion, qsort, heap_sort]


def main(arguments):
	SortingUtilClass.print_title(5, 'Sorting Analysis')
	for sortfn in SORTS:
		for size in LIST_SIZES:
			total = dict(comparisons=0)
			average = dict(comparisons=0)
			for i in range(ANALYSIS_TIMES):
				total['comparisons'] += sortfn(size)
			average['comparisons'] = total['comparisons']/size


if __name__ == '__main__':
	parser = ArgumentParser(description='Tester for Assignment #5')
	args = parser.parse_args()
	main(args)