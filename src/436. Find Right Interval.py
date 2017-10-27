# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from bisect import bisect_left
class Solution(object):
	def findRightInterval(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[int]
		"""
		N = len(intervals)
		starts = [(i.start, k) for k, i in enumerate(intervals)]
		starts.sort()
		return [-1 if idx == N else starts[idx][1] for i in intervals for idx in (bisect_left(starts, (i.end, 0)), )]


class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
print Solution().findRightInterval([Interval(a,b) for a, b in [ [1,4], [2,3], [3,4] ] ] )

