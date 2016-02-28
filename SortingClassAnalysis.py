from SortingClass import *
from argparse import ArgumentParser
from random import sample


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


def main(arguments):
	SortingUtilClass.print_title(5, 'Sorting Analysis')
	LIST_SIZES = [10, 50, 100, 500, 1000]
	SORT_RESULTS = {'bubble':[], 'selection':[], 'insertion':[], 'qsort':[], 'heap':[]}
	SORT_AVERAGES = {'bubble':[], 'selection':[], 'insertion':[], 'qsort':[], 'heap':[]}
	# bubble
	for size in LIST_SIZES:
		res = bubble(size)
		avg = res / size
		SORT_RESULTS['bubble'].append(res)
		SORT_AVERAGES['bubble'].append(avg)

	# selection
	for size in LIST_SIZES:
		res = selection(size)
		avg = res / size
		SORT_RESULTS['selection'].append(res)
		SORT_AVERAGES['selection'].append(avg)

	# insertion
	for size in LIST_SIZES:
		res = insertion(size)
		avg = res / size
		SORT_RESULTS['insertion'].append(res)
		SORT_AVERAGES['insertion'].append(avg)

	# qsort
	for size in LIST_SIZES:
		res = qsort(size)
		avg = res / size
		SORT_RESULTS['qsort'].append(res)
		SORT_AVERAGES['qsort'].append(avg)

	# heap
	for size in LIST_SIZES:
		res = heap_sort(size)
		avg = res / size
		SORT_RESULTS['heap'].append(res)
		SORT_AVERAGES['heap'].append(avg)

	print('Comparisons:')
	for sort in SORT_RESULTS:
		print('\t{}: '.format(sort))
		for res in SORT_RESULTS[sort]:
			print('\t\t{}'.format(res))
			
	print('Averages:')
	for sort in SORT_AVERAGES:
		print('\t{}: '.format(sort))
		for res in SORT_AVERAGES[sort]:
			print('\t\t{}'.format(res))


if __name__ == '__main__':
	parser = ArgumentParser(description='Tester for Assignment #5')
	args = parser.parse_args()
	main(args)
