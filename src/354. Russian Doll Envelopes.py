from bisect import bisect_left
class Solution(object):
	def maxEnvelopes(self, envelopes):
		"""
		:type envelopes: List[List[int]]
		:rtype: int
		"""
		envelopes.sort(key=lambda e: (e[0], -e[1]))
		heights = [wh[1] for wh in envelopes]
		# print envelopes, heights
		bs = []
		for h in heights:
			i = bisect_left(bs, h)
			if i == len(bs):
				bs.append(h)
			else:
				bs[i] = h

		return len(bs)



print Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3],[2,4]])
