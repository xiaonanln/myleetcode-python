class NumMatrix(object):

	def __init__(self, matrix):
		"""
		:type matrix: List[List[int]]
		"""
		self.matrix = matrix 
		ROWS = len(matrix)
		if not ROWS: return 
		
		COLS = len(matrix[0])
		self.dp = dp = [ [0] * COLS for _ in xrange(ROWS) ]
		for row in xrange(ROWS):
			for col in xrange(COLS):
				v = matrix[row][col]
				if row == 0 and col == 0:
					self.dp[row][col] = matrix[0][0]
				elif row == 0:
					self.dp[row][col] = dp[row][col-1] + v
				elif col == 0:
					self.dp[row][col] = dp[row-1][col] + v
				else:
					self.dp[row][col] = dp[row-1][col] + dp[row][col-1] - dp[row-1][col-1] + v
		# print self.dp

	def sumRegion(self, row1, col1, row2, col2):
		"""
		:type row1: int
		:type col1: int
		:type row2: int
		:type col2: int
		:rtype: int
		"""
		dp = self.dp
		if row1 == 0 and col1 == 0:
			return dp[row2][col2]
		elif row1 == 0:
			return dp[row2][col2] - dp[row2][col1-1]
		elif col1 == 0:
			return dp[row2][col2] - dp[row1-1][col2]
		else:
			return dp[row2][col2] - dp[row2][col1-1] - dp[row1-1][col2] + dp[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

matrix = NumMatrix(matrix)
print matrix.sumRegion(0, 0, 0, 4)
print matrix.sumRegion(2, 1, 4, 3)
print matrix.sumRegion(1, 1, 2, 2)
print matrix.sumRegion(1, 2, 2, 4)