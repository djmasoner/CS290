# student_list.py
# ===================================================
# Reimplementation of Pythons List
# ===================================================

import numpy as np


# StudentList class is our implementation of Python's List
class StudentList:
	def __init__(self):
		# creates an empty array of length 4, change the [4] to another value to make an
		# array of different length.
		self._list = np.empty([4], np.int16)
		self._capacity = 4
		self._size = 0

	def __str__(self):
		return str(self._list[:self._size])

# You may want an internal function that handles resizing the array.
# Dont modify get_list or get_capacity, they are for testing

	def get_list(self):
		return self._list[:self._size]

	def get_capacity(self):
		return self._capacity

	def get_array(self):
		return self._list

	def append(self, input):
		if self._size == self._capacity:
			self._capacity = self._capacity * 2
			self._list = np.append(self._list, input)
			self._size += 1
		else:
			self._list = np.append(self._list, input)
			self._size += 1


	def pop(self):
		self._size = self._size - 1
		self._list = np.delete(self._list, -1)
		return self._list[self._size]

	def insert(self, index, input):
		if index <= self._capacity:
			if index <= self._size:
				self._list[index] = input
				return
			self._list = np.insert(self._list, index, input)
			self._size = self._size + 1
		self.append()

	def remove(self, input):
		for i in range(0, self._size):
			if self.get(i) == input:
				np.delete(self._list, i)
				self._size = self._size - 1
			return


	def clear(self):
		while (len(self._list) != 0):
			self._list = np.delete(self._list)

	def count(self):
		return self._size

	def get(self, index):
		return self._list[index]

