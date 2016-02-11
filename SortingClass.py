from copy import copy


class SortingUtilClass:

	@staticmethod
	def list_to_string(values):
		count = len(values) - 1
		res = ''
		for n in values:
			fmt_string = '{:<3}'
			res += fmt_string.format(n)
		return res

	@staticmethod
	def print_results(comparisons, swaps):
		print()
		print('Analysis: ')
		print('\t{0:<12}  {1:>3}'.format('Comarisons:', comparisons))
		print('\t{0:<12}  {1:>3}'.format('Swaps:', swaps))
		print('\t{0:<12}  {1:>3}'.format('Work:', comparisons + (5 * swaps)))
		print()

	@staticmethod
	def print_title(assign_num, title):
		print('Tyberius Enders')
		print('Assignment {} - {}'.format(assign_num, title))
		print()

	@staticmethod
	def print_loop_position(num, array):
		print('Loop #{0}    Array = {1}'.format(num, SortingUtilClass.list_to_string(array)))

	@staticmethod
	def print_comparison_level(array, comparison, spacing):
		pass

	@staticmethod
	def print_char_line(char):
		for i in range(1,55):
			print(char, end='')
		print()

	@staticmethod
	def print_algorithm_title(title):
		SortingUtilClass.print_char_line('#')
		print(title)
		print()


class SortingClass:

	def __init__(self):
		self.comparisons = 1
		self.swaps = 1
		self.level = 1

	def set_defaults(self):
		self.comparisons = 1
		self.swaps = 1
		self.level = 1

	def finish(self):
		SortingUtilClass.print_results(self.comparisons, self.swaps)
		work = self.comparisons+(5*self.swaps)
		return dict(comparisons=self.comparisons, swaps=self.swaps, work=work, level=self.level)

	def bubble_sort(self, values):
		n = len(values)
		for i in range(n):
			# print loop level
			for j in range(1,n):
				# print comparison
				self.comparisons += 1
				if values[j-1] > values[j]:
					values[j-1], values[j] = values[j], values[j-1]
					# print swaps
					self.swaps += 1
		return self

	def insertion_sort(self, values):
		n = len(values)
		for i in range(1,n):
			j = i
			while j > 0 and values[j-1] > values[j]:
				# print comparison
				self.comparisons += 1
				# swap values
				values[j-1], values[j] = values[j], values[j-1]
				self.swaps += 1
				j -= 1
			else:
				# print comparison
				self.comparisons += 1
		return self

	def selection_sort(self, values):
		n = len(values)
		count = 1
		for i in range(n-1, 0, -1):
			# print loop level
			maximum = self.max_key(0, i, values)
			# swap values
			values[maximum], values[i] = values[i], values[maximum]
			self.swaps += 1
			count += 1
		return self

	def max_key(self, low, high, values):
		largest = low
		for j in range(low+1, high+1):
			# print comparison
			self.comparisons += 1
			if values[largest] < values[j]:
				largest = j
			# print max and array
		return largest

	# Assignment 4 methods
	def partition(self, values, low, high):
		pivot = values[high]
		i = low

		# print pivot
		for j in range(low, high):
			# print comparison

			self.comparisons += 1
			if values[j] <= pivot:
				values[i], values[j] = values[j], values[i]
				self.swaps += 1
				i += 1

		# swap values
		values[i], values[high] = values[high], values[i]
		self.swaps += 1
		return i

	def quick_sort(self, values, low, high):
		# print level
		# print array
		# print low
		# print high
		if low < high:
			p = self.partition(values, low, high)
			self.level += 1
			# print 'Calling QS'...
			self.quick_sort(values, low, p - 1)
			self.quick_sort(values, p + 1, high)
		return self

	def all(self, orig):
		values = copy(orig)
		self.set_defaults()
		SortingUtilClass.print_algorithm_title('Bubble Sort')
		self.bubble_sort(values).finish()

		values = copy(orig)
		self.set_defaults()
		SortingUtilClass.print_algorithm_title('Insertion Sort')
		self.insertion_sort(values).finish()

		values = copy(orig)
		self.set_defaults()
		SortingUtilClass.print_algorithm_title('Selection Sort')
		self.selection_sort(values).finish()

		values = copy(orig)
		self.set_defaults()
		SortingUtilClass.print_algorithm_title('Quick Sort')
		self.quick_sort(values, 0, len(values) - 1).finish()
