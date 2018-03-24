
from heapq import heappush, heappop, heappushpop
class MedianFinder(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.left = []
		self.right = []

	def addNum(self, num):
		"""
		:type num: int
		:rtype: void
		"""
		assert len(self.right) == len(self.left) or len(self.right) == len(self.left) + 1

		if len(self.left) == len(self.right):
			if self.left and num >= -self.left[0]:
				heappush(self.right, num)
			else:
				popnum = -heappushpop(self.left, -num)
				heappush(self.right, popnum)

		else: # len(self.left) + 1 == len(self.right):
			if num <= self.right[0]:
				heappush(self.left, -num)
			else:
				popnum = heappushpop(self.right, num)
				heappush(self.left, -popnum)

		assert len(self.right) == len(self.left) or len(self.right) == len(self.left) + 1

	def findMedian(self):
		"""
		:rtype: float
		"""
		if len(self.right) == len(self.left):
			return (-self.left[0] + self.right[0]) / 2.0
		else:
			return self.right[0]

mf = MedianFinder()
mf.addNum(6)
mf.addNum(10)
mf.addNum(2)
mf.addNum(6)
print mf.left, mf.right
mf.addNum(5)
print mf.left, mf.right
print mf.findMedian()
