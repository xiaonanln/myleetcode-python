from heapq import *
class Solution(object):
	def getSkyline(self, buildings):
		"""
		:type buildings: List[List[int]]
		:rtype: List[List[int]]
		"""
		if not buildings:
			return []

		N = len(buildings)
		l,r,h = buildings[0]
		skyline = []
		heap = []   

		i = 0
		while True:
			if not heap and i >= N: break
			t = float('inf')
			if heap:
				t = min(t, heap[0][1])
			if i < N:
				t = min(t,  buildings[i][0])

			# print 't', t
			while heap and heap[0][1] <= t:
				heappop( heap )

			while i < N and buildings[i][0] <= t:
				heappush(heap, (-buildings[i][2], buildings[i][1]))
				i += 1

			h_ = -heap[0][0] if heap else 0
			# print t, h_, heap
			if not skyline or skyline[-1][1] != h_:
				skyline.append((t, h_))

		return skyline


print Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
print [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

