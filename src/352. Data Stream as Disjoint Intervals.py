
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class _ufnode(object):
	__slots__ = ('L', 'R', 'parent')

	def __init__(self, L, R):
		self.L = L
		self.R = R
		self.parent = None

class SummaryRanges(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.rangeOfVal = {}

	def addNum(self, val):
		"""
		:type val: int
		:rtype: void
		"""
		if val in self.rangeOfVal:
			return

		leftRange = self.getRange(val-1)
		rightRange = self.getRange(val+1)
		node = _ufnode(val if leftRange is None else leftRange.L,
		               val if rightRange is None else rightRange.R)
		if leftRange is not None:
			leftRange.parent = node
		if rightRange is not None:
			rightRange.parent = node
		self.rangeOfVal[val] = node

	def getRange(self, val):
		if val not in self.rangeOfVal:
			return None

		r = self.rangeOfVal[val]
		if r.parent:
			while r.parent:
				r = r.parent

			self.rangeOfVal[val] = r

		return r

	def getIntervals(self):
		"""
		:rtype: List[Interval]
		"""


obj = SummaryRanges()
for val in [1, 3, 7, 2, 6]:
	obj.addNum(val)
	print obj.getIntervals()

