from SortingClass import *
from argparse import ArgumentParser
from random import sample

ANALYSIS_TIMES = 10
LIST_SIZES = [10, 50, 100, 500, 1000]
RESULTS = []
AVERAGE_RESULTS = []
# LIST_SIZES = [10]


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
	analysis = s.quick_sort(array, 0, len(array) - 1).get_analysis()
	comparisons = analysis['comparisons']
	return comparisons


def heap_sort(size):
	array = sample(range(size), size)
	s = SortingClass(to_print=False)
	analysis = s.heap_sort(array, len(array)).get_analysis()
	comparisons = analysis['comparisons']
	return comparisons

SORTS = [bubble, selection, insertion, qsort, heap_sort]
# SORTS = [bubble, selection]


def main(arguments):
	SortingUtilClass.print_title(5, 'Sorting Analysis')
	for index in range(len(SORTS)):
		total_comparisons = {'bubble': 0, 'selection': 0, 'insertion': 0, 'qsort': 0, 'heap': 0}
		average_comparisons = {'bubble': 0, 'selection': 0, 'insertion': 0, 'qsort': 0, 'heap': 0}
		for size in LIST_SIZES:
			total = dict(comparisons=0)
			average = dict(comparisons=0)
			for i in range(ANALYSIS_TIMES):
				total['comparisons'] += SORTS[index](size)
				if index == 0:
					total_comparisons['bubble'] = total['comparisons']
					average_comparisons['bubble'] = average['comparisons']
				elif index == 1:
					total_comparisons['selection'] = total['comparisons']
					average_comparisons['selection'] = average['comparisons']
				elif index == 2:
					total_comparisons['insertion'] = total['comparisons']
					average_comparisons['insertion'] = average['comparisons']
				elif index == 3:
					total_comparisons['qsort'] = total['comparisons']
					average_comparisons['qsort'] = average['comparisons']
				elif index == 4:
					total_comparisons['heap'] = total['comparisons']
					average_comparisons['heap'] = average['comparisons']
			average['comparisons'] = total['comparisons']/size

		RESULTS.append(total_comparisons)
		AVERAGE_RESULTS.append(average_comparisons)

	print(RESULTS)
	print(AVERAGE_RESULTS)


if __name__ == '__main__':
	parser = ArgumentParser(description='Tester for Assignment #5')
	args = parser.parse_args()
	main(args)