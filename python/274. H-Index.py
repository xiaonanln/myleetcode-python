from collections import Counter
class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		citations = Counter(citations)
		citations = citations.items()
		citations.sort(reverse=True)
		# print citations
		t = 0
		res = 0
		for h, n in citations:
			if h < res: break
			t += n
			# has t paper >= h
			res = max(res, min(t, h))

		return res

# print Solution().hIndex([4, 4, 0, 0])
print Solution().hIndex([0])

