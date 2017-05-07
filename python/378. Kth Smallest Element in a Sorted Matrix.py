
import time 

from heapq import *
class Solution(object):
	def kthSmallest(self, matrix, k):
		"""
		:type matrix: List[List[int]]
		:type k: int
		:rtype: int
		"""
		heap = []
		R = len(matrix)
		p = [0] * R

		while k > 0:
			# time.sleep(0.1)
			maxn = None 
			for r in xrange(R):
				# print k, r, p, heap
				if p[r] >= R: continue 
				if maxn is None:
					maxn = matrix[r][p[r]]
					heappush(heap, maxn)
					p[r] += 1
				else:
					# print r, p[r], 'maxn', maxn, matrix[r][p[r]]
					while p[r] < R and matrix[r][p[r]] <= maxn:
						heappush(heap, matrix[r][p[r]])
						p[r] += 1

			while k > 0 and heap:
				minn = heappop(heap)
				# print 'pop', minn, k
				k -= 1
				if k == 0: 
					return minn



matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15], 
]
k = 8
print Solution.kthSmallest(Solution(), matrix, k)
