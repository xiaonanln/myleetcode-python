from collections import Counter

class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		C = Counter(nums)
		U = C.keys()
		U.sort(key=lambda x:C[x], reverse=True)
		return U[:k]

print Solution().topKFrequent([1], 1)
print Solution().topKFrequent([1,1,2], 1)
print Solution().topKFrequent([1,1,1,2,2,3], 2)