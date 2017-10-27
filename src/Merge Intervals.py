# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals = [ [i.start, i.end] for i in intervals]
        if not intervals: return []
        
        intervals.sort(cmp=lambda int1, int2: cmp(int1[0], int2[0]) )
        merged = [ list(intervals[0]) ]
        last = merged[0]
        
        for i, interval in enumerate(intervals, 1):
            if interval[0] <= last[1]:
                last[1] = max(last[1], interval[1])
            else:
                merged.append( list(interval) )
                last = merged[-1]
        
        return [ Interval(r[0], r[1])  for r in merged ]

    
given = [[1,3],[2,6],[8,10],[15,18]]
print Solution().merge( [[1,3]] )