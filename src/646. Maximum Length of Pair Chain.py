import operator
class Solution(object):
	def findLongestChain(self, pairs):
		"""
		:type pairs: List[List[int]]
		:rtype: int
		"""
		pairs.sort(key=operator.itemgetter(1))
		last = float('-inf')
		length = 0
		for a, b in pairs:
			if a <= last: continue
			# a > last
			last = b
			length += 1

		return length


print Solution().findLongestChain([[1,2], [2,3], [3,4]])