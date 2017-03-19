# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

       	ret = []

        rangeMin, rangeMax = newInterval.start, newInterval.end
        i = 0
        while i < len(intervals) and intervals[i].end < rangeMin:
        	ret.append(intervals[i])
        	i += 1

        while i < len(intervals) and intervals[i].start <= rangeMax:
        	rangeMin = min(intervals[i].start, rangeMin)
        	rangeMax = max(intervals[i].end, rangeMax)
        	i += 1

        ret.append([rangeMin, rangeMax])
        return ret + intervals[i:]
        
print Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9])
