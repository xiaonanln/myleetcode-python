class NumMatrix(object):
	def __init__(self, matrix):
		"""
		:type matrix: List[List[int]]
		"""
		self.M = matrix
		R = len(matrix)
		if R:
			C = len(matrix[0])
		else:
			C = 0
		self.S = [ [None] * (C+1) for _ in xrange(R+1) ]
		for r in xrange(R+1):
			self.S[r][0] = 0

		for c in xrange(C+1):
			self.S[0][c] = 0

	def sumRegion(self, row1, col1, row2, col2):
		"""
		:type row1: int
		:type col1: int
		:type row2: int
		:type col2: int
		:rtype: int
		"""
		return self.sumRegionHelper( row2+1, col2+1 ) + self.sumRegionHelper( row1, col1 ) - self.sumRegionHelper(row1, col2+1) - self.sumRegionHelper(row2+1, col1)

	def sumRegionHelper(self, r, c):

		if self.S[r][c] is not None:
			return self.S[r][c]

		s = self.M[r-1][c-1] + self.sumRegionHelper(r-1, c) + self.sumRegionHelper(r, c-1) - self.sumRegionHelper(r-1, c-1)
		self.S[r][c] = s
		return s


matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
nm = NumMatrix(matrix)
print nm.sumRegion(2, 1, 4, 3)
print nm.sumRegion(1, 1, 2, 2)
print nm.sumRegion(1, 2, 2, 4)