# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
	def __init__(self, iterator):
		"""
		Initialize your data structure here.
		:type iterator: Iterator
		"""
		self.it = iterator
		self.peeked = False
		self.peekedVal = None

	def peek(self):
		"""
		Returns the next element in the iteration without advancing the iterator.
		:rtype: int
		"""
		if not self.peeked and self.it.hasNext():
			self.peeked = True
			self.peekedVal = self.it.next()
		return self.peekedVal

	def next(self):
		"""
		:rtype: int
		"""
		if self.peeked:
			nextVal = self.peekedVal
			self.peeked = False
			self.peekedVal = None
			return nextVal
		else:
			return self.it.next()

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return self.peeked or self.it.hasNext()
