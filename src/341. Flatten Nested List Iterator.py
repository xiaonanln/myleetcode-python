# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
	def __init__(self, nestedList):
		"""
		Initialize your data structure here.
		:type nestedList: List[NestedInteger]
		"""
		self.gen = self.iter(nestedList)
		self.genNext = None

	def iter(self, nestedList):
		for elem in nestedList:
			if isinstance(elem, NestedInteger):
				if elem.isInteger():
					yield elem.getInteger()
				else:
					for n in self.iter(elem.getList()):
						yield n
			else:
				yield elem

	def next(self):
		"""
		:rtype: int
		"""
		return self.genNext

	def hasNext(self):
		"""
		:rtype: bool
		"""
		try:
			self.genNext = self.gen.next()
			return True
		except StopIteration:
			return False


	# Your NestedIterator object will be instantiated and called as such:
	# i, v = NestedIterator(nestedList), []
	# while i.hasNext(): v.append(i.next())

i = NestedIterator([1,2,[3,4,[5,6]]])
while i.hasNext():
	print i.next()


