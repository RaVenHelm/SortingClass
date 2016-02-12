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
	def print_comparison_level(array, comparison, spacing, print_list, adjust):
		print('Comparison'.rjust(14), end=' ')
		print('#{}'.format(comparison).ljust(spacing), end='')
		print('{}'.format(SortingUtilClass.list_to_string(print_list)).rjust(adjust))

	@staticmethod
	def print_comparison_simple(comparison, values, low, high):
		fmt = 'Comparison #{}'.format(comparison)
		if (comparison / 10) < 1:
			print(fmt.rjust(18), end='')
		else:
			print(fmt.rjust(19), end='')

		base_spaces = 3*low + 6

		print('{}'.format(values[low]).rjust(base_spaces), end='')
		print('{}'.format(values[high]).rjust(3*(high - low)))

	@staticmethod
	def print_swap_simple(swap, values, low, high):
		fmt = 'Swap #{}'.format(swap)
		if (swap / 10) < 1:
			print(fmt.rjust(12), end='')
		else:
			print(fmt.rjust(13), end='')
		print('{}'.format(values[low]).rjust(3*low+12), end='')
		print('{}'.format(values[high]).rjust(3*(high-low)))

	@staticmethod
	def print_swap_level(array, swap, spacing, print_list, adjust):
		print('Swap'.rjust(8), end=' ')
		print('#{}'.format(swap).ljust(spacing), end='')
		print('{}'.format(SortingUtilClass.list_to_string(print_list).rjust(adjust)))

	@staticmethod
	def print_pivot_level(pivot):
		pivot_spaces = 14
		if (pivot / 10) >= 1:
			pivot_spaces = 15
		print('Pivot = {}'.format(pivot).rjust(pivot_spaces))

	@staticmethod
	def print_level_with_array(level, array):
		print('Level {}:'.format(level), end='')
		print('Array = {}'.format(SortingUtilClass.list_to_string(array)).rjust(15 + len(array) * 3))

	@staticmethod
	def print_high_low(high, low):
		low_spaces = 12
		if (low / 10) >= 1:
			low_spaces = 11
		print('Low = {}'.format(low).rjust(low_spaces))

		high_spaces = 13
		if (high / 10) >= 1:
			high_spaces = 14
		print('High = {}'.format(high).rjust(high_spaces))

	@staticmethod
	def print_qs_fn(low, high, index):
		a = low
		b = index - 1
		c = index + 1
		d = high
		if a > b:
			a, b = b, a
		if c > d:
			c, d = d, c
		print('Calling QS ({}-{}) and ({}-{})'.format(a, b, c, d))

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

	def __init__(self, to_print=True):
		self.comparisons = 1
		self.swaps = 1
		self.level = 1
		self.print = to_print

	def set_defaults(self):
		self.comparisons = 1
		self.swaps = 1
		self.level = 1

	def finish(self):
		if self.print:
			SortingUtilClass.print_results(self.comparisons, self.swaps)
		work = self.comparisons+(5*self.swaps)
		return dict(comparisons=self.comparisons, swaps=self.swaps, work=work, level=self.level)

	def bubble_sort(self, values):
		n = len(values)
		for i in range(n):
			# print loop level
			if self.print:
				SortingUtilClass.print_loop_position(i+1,values)
			for j in range(1,n):
				# print comparison
				if self.print:
					SortingUtilClass.print_comparison_level(values, self.comparisons, 3*(j - 2) + 7, [values[j-1], values[j]], j)
				self.comparisons += 1
				if values[j-1] > values[j]:
					values[j-1], values[j] = values[j], values[j-1]
					# print swaps
					if self.print:
						SortingUtilClass.print_swap_level(values, self.swaps, 3*(j - 2) + 13, [values[j-1], values[j]], j)
					self.swaps += 1
		return self

	def insertion_sort(self, values):
		n = len(values)
		for i in range(1,n):
			j = i
			if self.print:
				SortingUtilClass.print_loop_position(j, values)
			while j > 0 and values[j-1] > values[j]:
				# print comparison
				if self.print:
					SortingUtilClass.print_comparison_level(values, self.comparisons, 3*(j - 1) + 4, [values[j-1], values[j]], j)
				self.comparisons += 1
				# swap values
				values[j-1], values[j] = values[j], values[j-1]
				# print swaps
				if self.print:
					SortingUtilClass.print_swap_level(values, self.swaps, 3*(j - 1) + 10, [values[j-1], values[j]], j)
				self.swaps += 1
				j -= 1
			else:
				# print comparison
				if self.print:
					SortingUtilClass.print_comparison_level(values, self.comparisons, 3*(j - 1) + 4, [values[j-1], values[j]], j)
				self.comparisons += 1
		return self

	def selection_sort(self, values):
		n = len(values)
		count = 1

		for i in range(n-1, 0, -1):
			# print loop level
			if self.print:
				SortingUtilClass.print_loop_position(count, values)
			maximum = self.max_key(0, i, values)
			# swap values
			values[maximum], values[i] = values[i], values[maximum]
			# print swaps
			if self.print:
				SortingUtilClass.print_swap_level(values, self.swaps, 3*(i-1) + 10, [values[maximum], values[i]], i)
			self.swaps += 1
			count += 1
		return self

	def max_key(self, low, high, values):
		largest = low
		for j in range(low+1, high+1):
			# print comparison
			if self.print:
				SortingUtilClass.print_comparison_level(values, self.comparisons, 3*(j - 1) + 4, [values[j-1], values[j]], j)
			self.comparisons += 1
			if values[largest] < values[j]:
				largest = j
			# print max and array
			if self.print:
				pass
		return largest

	# Assignment 4 methods
	def partition(self, values, low, high):
		pivot = values[high]
		i = low

		# print pivot
		SortingUtilClass.print_pivot_level(pivot)
		for j in range(low, high):
			# print comparison
			if self.print:
				SortingUtilClass.print_comparison_simple(self.comparisons, values, j, high)
				# SortingUtilClass.print_comparison_level(values, self.comparisons, 3*(j-1) + 10, [values[j], pivot], j)
			self.comparisons += 1
			if values[j] <= pivot:
				values[i], values[j] = values[j], values[i]
				i += 1

		# swap values
		values[i], values[high] = values[high], values[i]
		if self.print:
			# SortingUtilClass.print_swap_level(values, self.swaps, 3*(i-1) + 10, [values[i], values[high]], i)
			SortingUtilClass.print_swap_simple(self.swaps, values, i, high)
		self.swaps += 1
		return i

	def quick_sort(self, values, low, high):
		# print level
		# print array
		# print low
		# print high
		if self.print:
			SortingUtilClass.print_level_with_array(self.level, values)
			SortingUtilClass.print_high_low(high, low)
		if low < high:
			p = self.partition(values, low, high)
			self.level += 1
			# print 'Calling QS'...
			if self.print:
				SortingUtilClass.print_qs_fn(low, high, p)
			self.quick_sort(values, low, p - 1)
			self.quick_sort(values, p + 1, high)
		return self

	# Heap sort methods (Extra)
	def heap_sort(self, values, count):
		self.heapify(values, count)
		end = count - 1
		while end > 0:
			values[end], values[0] = values[0], values[end]
			self.swaps += 1
			end -= 1
			self.sift_down(values, 0, end)
		return self

	def heapify(self, values, count):
		start = int((count - 2) / 2)

		while start >= 0:
			self.sift_down(values, start, count - 1)
			start -= 1

	def sift_down(self, values, start, end):
		root = start

		while root * 2 + 1 <= end:
			child = root * 2 + 1

			if child + 1 <= end and values[child] < values[child + 1]:
				child += 1
				self.comparisons += 1
			if values[root] < values[child]:
				values[root], values[child] = values[child], values[root]
				self.swaps += 1
				root = child
				self.comparisons += 1
			else:
				return

	def all(self, orig):
		values = copy(orig)
		self.set_defaults()
		if self.print:
			SortingUtilClass.print_algorithm_title('Bubble Sort')
		self.bubble_sort(values).finish()

		values = copy(orig)
		self.set_defaults()
		if self.print:
			SortingUtilClass.print_algorithm_title('Insertion Sort')
		self.insertion_sort(values).finish()

		values = copy(orig)
		self.set_defaults()
		if self.print:
			SortingUtilClass.print_algorithm_title('Selection Sort')
		self.selection_sort(values).finish()

		values = copy(orig)
		self.set_defaults()
		if self.print:
			SortingUtilClass.print_algorithm_title('Quick Sort')
		self.quick_sort(values, 0, len(values) - 1).finish()

		values = copy(orig)
		self.set_defaults()
		if self.print:
			SortingUtilClass.print_algorithm_title('Heap Sort')
		self.heap_sort(values, len(values)).finish()
