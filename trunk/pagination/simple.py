#!/usr/bin/env python
""" pagination.simple - basic pagination """

__author__ 		= "Dexter Tad-y"
__credits__		= ["Leon Brocard", "Leo Lapworth"]
__license__ 	= "GPL"
__version__ 	= 0.1

import unittest

class Page:
	_total_entries 		= None
	_entries_per_page 	= None
	_current_page		= None

	def __init__(self, total_entries=0, entries_per_page=10, current_page=1):
		self.total_entries(total_entries)
		self.entries_per_page(entries_per_page)
		self.current_page(current_page)

	def total_entries(self, value=None):
		if value != None:
			self._total_entries = value
		return self._total_entries

	def entries_per_page(self, value=None): 
		if value != None:
			if value < 1:
				raise ValueError("fewer than one entry per page")
			self._entries_per_page = value
		return self._entries_per_page

	def current_page(self, value=None):
		# try set
		if value != None:
			self._current_page = value
			return self._current_page
		# get
		if self._current_page == None:
			return self.first_page()
		elif self._current_page < self.first_page():
			return self.first_page()
		elif self._current_page > self.last_page():
			return self.last_page()
		else:
			return self._current_page

	def first_page(self):
		return 1

	def last_page(self):
		pagesf = self.total_entries() / (self.entries_per_page() * 1.0)
		pages = int(pagesf)
		last_page = None
		if pagesf == pages:
			last_page = pages
		else:
			last_page = pages + 1
		if last_page < 1:
			last_page = 1
		return last_page

	def first_entry(self):
		if self.total_entries() == 0:
			return 0
		else:
			return ((self.current_page() - 1) * self.entries_per_page()) + 1

	def last_entry(self):
		if self.current_page() == self.last_page():
			return self.total_entries()
		else:
			return (self.current_page() * self.entries_per_page())

	def previous_page(self):
		if (self.current_page() > 1):
			return self.current_page - 1
		else:
			return None

	def next_page(self):
		if self.current_page() < self.last_page():
			return self.current_page() + 1

	def skipped(self):
		skipped = self.first - 1
		if skipped < 0:
			return 0
		return skipped
		


class PageTest(unittest.TestCase):
	def test_construct1(self):
		i = Page()
		self.assertEquals(i.total_entries(), 0)
		self.assertEquals(i.entries_per_page(), 10)
		self.assertEquals(i.current_page(), 1)

	def test_construct2(self):
		i = Page(123)
		self.assertEquals(i.total_entries(), 123)
		self.assertEquals(i.entries_per_page(), 10)
		self.assertEquals(i.current_page(), 1)

	def test_construct3(self):
		i = Page(123, 12)
		self.assertEquals(i.total_entries(), 123)
		self.assertEquals(i.entries_per_page(), 12)
		self.assertEquals(i.current_page(), 1)

	def test_construct4(self):
		i = Page(123, 12, 9)
		self.assertEquals(i.total_entries(), 123)
		self.assertEquals(i.entries_per_page(), 12)
		self.assertEquals(i.current_page(), 9)

	def test_error_entries(self):
		i = Page()
		self.assertRaises(ValueError, i.entries_per_page, 0)

	def test_basic_1(self):
		""" TODO!!!!!!!!!!!!!!!!!!!!!!!!!! """
		pass


if __name__ == "__main__":
	unittest.main()

