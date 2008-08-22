#!/usr/bin/env python
""" simple pagination """

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
			return self.current_page() - 1
		else:
			return None

	def next_page(self):
		if self.current_page() < self.last_page():
			return self.current_page() + 1

	def skipped(self):
		skipped = self.first_entry() - 1
		if skipped < 0:
			return 0
		return skipped
		


class PageTest(unittest.TestCase):
	BASICTEST = [
		# rip-off from t/simple.t of Data::Page distribution

		# Initial test
		[ 50, 10, 1, 1, 5, 1, 10, None, 1, 2, 	[ 0,1,2,3,4,5,6,7,8,9, ], 10 ],
		[ 50, 10, 2, 1, 5, 11, 20, 1, 2, 3, 	[ 10,11,12,13,14,15,16,17,18,19, ], 10 ],
		[ 50, 10, 3, 1, 5, 21, 30, 2, 3, 4, 	[ 20,21,22,23,24,25,26,27,28,29, ], 10 ],
		[ 50, 10, 4, 1, 5, 31, 40, 3, 4, 5, 	[ 30,31,32,33,34,35,36,37,38,39, ], 10 ],
		[ 50, 10, 5, 1, 5, 41, 50, 4, 5, None,  [ 40,41,42,43,44,45,46,47,48,49, ], 10 ],

		# Under 10
		[ 1, 10, 1, 1, 1, 1, 1, None, 1, None, 	[ 0, ], 1 ],
		[ 2, 10, 1, 1, 1, 1, 2, None, 1, None, 	[ 0,1, ], 2 ],
		[ 3, 10, 1, 1, 1, 1, 3, None, 1, None, 	[ 0,1,2, ], 3 ],
		[ 4, 10, 1, 1, 1, 1, 4, None, 1, None, 	[ 0,1,2,3, ], 4 ],
		[ 5, 10, 1, 1, 1, 1, 5, None, 1, None, 	[ 0,1,2,3,4, ], 5 ],
		[ 6, 10, 1, 1, 1, 1, 6, None, 1, None, 	[ 0,1,2,3,4,5, ], 6 ],
		[ 7, 10, 1, 1, 1, 1, 7, None, 1, None, 	[ 0,1,2,3,4,5,6, ], 7 ],
		[ 8, 10, 1, 1, 1, 1, 8, None, 1, None, 	[ 0,1,2,3,4,5,6,7, ], 8 ],
		[ 9, 10, 1, 1, 1, 1, 9, None, 1, None, 	[ 0,1,2,3,4,5,6,7,8, ], 9 ],
		[ 10, 10, 1, 1, 1, 1, 10, None, 1, None, 	[ 0,1,2,3,4,5,6,7,8,9, ], 10 ],

		# Over 10
		[ 11, 10, 1, 1, 2, 1, 10, None, 1, 2, 	[ 0,1,2,3,4,5,6,7,8,9, ], 10 ],
		[ 11, 10, 2, 1, 2, 11, 11, 1, 2, None, 	[ 10, ], 1 ],
		[ 12, 10, 1, 1, 2, 1, 10, None, 1, 2, 	[ 0,1,2,3,4,5,6,7,8,9, ], 10 ],
		[ 12, 10, 2, 1, 2, 11, 12, 1, 2, None, 	[ 10,11, ], 2 ],
		[ 13, 10, 1, 1, 2, 1, 10, None, 1, 2, 	[ 0,1,2,3,4,5,6,7,8,9, ], 10 ],
		[ 13, 10, 2, 1, 2, 11, 13, 1, 2, None, 	[ 10,11,12, ], 3 ],

		# Under 20
		[ 19, 10, 1, 1, 2, 1, 10, None, 1, 2, 	[ 0,1,2,3,4,5,6,7,8,9, ], 10 ],
		[ 19, 10, 2, 1, 2, 11, 19, 1, 2, None, 	[ 10,11,12,13,14,15,16,17,18, ], 9 ],
		[ 20, 10, 1, 1, 2, 1, 10, None, 1, 2, 	[ 0,1,2,3,4,5,6,7,8,9, ], 10 ],
		[ 20, 10, 2, 1, 2, 11, 20, 1, 2, None, 	[ 10,11,12,13,14,15,16,17,18,19, ], 10 ],

		# Over 20
		[ 21, 10, 1, 1, 3, 1, 10, None, 1, 2, 	[ 0,1,2,3,4,5,6,7,8,9, ], 10 ],
		[ 21, 10, 2, 1, 3, 11, 20, 1, 2, 3, 	[ 10,11,12,13,14,15,16,17,18,19, ], 10 ],
		[ 21, 10, 3, 1, 3, 21, 21, 2, 3, None, 	[ 20, ], 1 ],
		[ 22, 10, 1, 1, 3, 1, 10, None, 1, 2, 	[ 0,1,2,3,4,5,6,7,8,9, ], 10 ],
		[ 22, 10, 2, 1, 3, 11, 20, 1, 2, 3, 	[ 10,11,12,13,14,15,16,17,18,19, ], 10 ],
		[ 22, 10, 3, 1, 3, 21, 22, 2, 3, None, 	[ 20,21, ], 2 ],
		[ 23, 10, 1, 1, 3, 1, 10, None, 1, 2, 	[ 0,1,2,3,4,5,6,7,8,9, ], 10 ],
		[ 23, 10, 2, 1, 3, 11, 20, 1, 2, 3, 	[ 10,11,12,13,14,15,16,17,18,19, ], 10 ],
		[ 23, 10, 3, 1, 3, 21, 23, 2, 3, None,  [ 20,21,22, ], 3 ],

		# Zero test
		[ 0, 10, 1, 1, 1, 0, 0, None, 1, None,  [ ], 0 ],

	]
		# ^^^^
		# Format of test data: 0=number of entries, 1=entries per page, 2=current page,
		# 3=first page, 4=last page, 5=first entry on page, 6=last entry on page,
		# 7=previous page, 8=current page, 9=next page, 10=current entries, 11=current number of entries


	def test_basic(self):
		t = self.BASICTEST
		for i in t:
			_total 	= i[0]
			_epp 	= i[1]
			_cp		= i[2]
			fp		= i[3]
			lp		= i[4]
			fe		= i[5]
			le		= i[6]
			pp		= i[7]
			cp		= i[8]
			np		= i[9]
			ce		= i[10]
			cnoe    = i[11]
			# ----
			p = Page(_total, _epp, _cp)
			self.assertEquals( p.first_page(), fp )
			self.assertEquals( p.last_page(), lp )
			self.assertEquals( p.first_entry(), fe )
			self.assertEquals( p.last_entry(), le )
			self.assertEquals( p.previous_page(), pp )
			self.assertEquals( p.current_page(), cp )
			entries = [ ] 
			if fe-1 >= 0: entries = range(fe-1, le)
			self.assertEquals( entries, ce )
			self.assertEquals( len(entries), cnoe )
			
		

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


if __name__ == "__main__":
	unittest.main()

