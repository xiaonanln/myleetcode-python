class Solution(object):
	def longestIncreasingPath(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: int
		"""
		R = len(matrix)
		if R == 0:
			return 0
		C = len(matrix[0])

		items = []
		for r in xrange(0, R):
			for c in xrange(0, C):
				items.append( (matrix[r][c], r, c) )
		items.sort(reverse=True)
		# print items 
		lip = [[1]*C for _ in xrange(R)] # min is 1
		maxlip = 1
		for v, r, c in items:

			for ar, ac in ( (r-1, c), (r+1, c), (r, c-1), (r, c+1) ):
				if ar < 0 or ac < 0 or ar >= R or ac >= C: continue 
				av = matrix[ar][ac]
				if av <= v: continue 
				# av > v
				lip[r][c] = max(lip[r][c], lip[ar][ac]+1)
				maxlip = max(maxlip, lip[r][c])

		return maxlip



nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
print Solution().longestIncreasingPath(nums)
nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
print Solution().longestIncreasingPath(nums)