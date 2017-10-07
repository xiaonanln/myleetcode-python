# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def eraseOverlapIntervals(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: int
		"""
		if not intervals: return 0
		intervals.sort(key=lambda i: (i.start, i.end))
		lastiv = intervals[0]
		remove = 0
		for i in xrange(1, len(intervals)):
			iv = intervals[i]
			if iv.start >= lastiv.end:
				lastiv = iv
			elif iv.end >= lastiv.end:
				# remove iv
				remove += 1
			else:
				# remove lastiv
				lastiv = iv
				remove += 1

		return remove

print Solution().eraseOverlapIntervals(map(lambda l: Interval(*l), [ [1,2], [2,3], [3,4], [1,3] ]))
print Solution().eraseOverlapIntervals(map(lambda l: Interval(*l), [ [1,2], [1,2], [1,2] ]))






