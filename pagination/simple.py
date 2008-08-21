#!/usr/bin/env python
""" pagination.simple - basic pagination """

__author__ 		= "Dexter Tad-y"
__license__ 	= "GPL"
__version__ 	= 0.1


import unittest

class Page:
	def __init__(self, total_entries=0, entries_per_page=10, current_page=1):
		self.total_entries=total_entries
		self.entries_per_page=entries_per_page
		self.current_page=current_page
	def get_entries_per_page(self):
		return self._entries_per_page
	def set_entries_per_page(self, entries_per_page):
		if (entries_per_page<1):
			raise ValueError("fewer than one entry per page")
	entries_per_page = property(get_entries_per_page, set_entries_per_page)


class PageTest(unittest.TestCase):
	def test_construct1(self):
		i = Page()
		self.assertEquals(i.total_entries, 0)
		self.assertEquals(i.entries_per_page, 10)
		self.assertEquals(i.current_page, 1)
	def test_construct2(self):
		i = Page(123)
		self.assertEquals(i.total_entries, 123)
		self.assertEquals(i.entries_per_page, 10)
		self.assertEquals(i.current_page, 1)
	def test_construct3(self):
		i = Page(123, 12)
		self.assertEquals(i.total_entries, 123)
		self.assertEquals(i.entries_per_page, 12)
		self.assertEquals(i.current_page, 1)
	def test_construct4(self):
		i = Page(123, 12, 9)
		self.assertEquals(i.total_entries, 123)
		self.assertEquals(i.entries_per_page, 12)
		self.assertEquals(i.current_page, 9)
	def test_properties(self):
		i = Page()
		#self.assertRaises(ValueError, i.entries_per_page, 0);
		pass
		


if __name__ == "__main__":
	unittest.main()

		
