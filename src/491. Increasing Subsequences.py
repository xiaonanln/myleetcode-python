class Solution(object):
	def findSubsequences(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		all = []
		last = []
		
		for n in nums:
			for i in xrange(len(last)):
				seq = last[i]
				if seq[-1] <= n:
					newseq = seq + (n, )
					all.append(newseq)
					last.append(newseq)
			last.append((n, ))
		return list(set(all))

print Solution().findSubsequences([4,5,7,7])