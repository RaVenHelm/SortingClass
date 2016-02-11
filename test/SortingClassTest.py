import unittest
from SortingClass import *


class SortingClassTest(unittest.TestCase):
	def setUp(self):
		self.sorter = SortingClass(False)

	def test_init_settings(self):
		self.assertEquals(self.sorter.comparisons, 1, 'set comparisons to 1')
		self.assertEquals(self.sorter.swaps, 1, 'set swaps to 1')
		self.assertEquals(self.sorter.level, 1, 'set level to 1')
		self.assertEquals(self.sorter.print, False, 'do not print for testing')

if __name__ == '__main__':
	unittest.main()
