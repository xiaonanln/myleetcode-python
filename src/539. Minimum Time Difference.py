import bisect
class Solution(object):
	def findMinDifference(self, timePoints):
		"""
		:type timePoints: List[str]
		:rtype: int
		"""
		secs = []
		for tp in timePoints:
			a, b = tp.split(':')
			sec = int(a) * 60 + int(b)
			secs.append(sec)

		secs.sort()
		N = len(secs)
		mind = float('inf')
		for i, sec in enumerate(secs):
			if i < N-1:
				d = secs[i+1] - secs[i]
			else:
				d = secs[0] + 1440 - secs[i]

			mind = min(mind, d)

		return mind


print Solution().findMinDifference(["23:59", "00:00"])