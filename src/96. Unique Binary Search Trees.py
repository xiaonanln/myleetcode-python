class Solution(object):
	def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 1: return 1

		nt = [0] * (n+1)
		nt[0] = 1
		nt[1] = 1
		for i in xrange(2, n+1):
			# i numbers
			total = 0
			for k in xrange(i):
				# let kth number be the root, left has k numbers, right has i-k-1 numbers
				total += nt[k] * nt[i-k-1]
			
			# print n, total
			nt[i] = total
		
		return nt[n]
		
			
# print Solution().numTrees(0)
# print Solution().numTrees(1)
# print Solution().numTrees(2)
print Solution().numTrees(3)
# print Solution().numTrees(4)