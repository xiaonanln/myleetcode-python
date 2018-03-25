# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
	def findCelebrity(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		a = 0
		for b in xrange(1, n):
			if knows(a, b):
				# a knows b, so b could be cele
				a = b

		return a if all(knows(i, a) and not knows(a,i) for i in xrange(n) if i != a) else -1
