class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""

		R = len(matrix)
		if not R: 
			return False
		C = len(matrix[0])
		minRow, maxRow = 0, R-1
		minCol, maxCol = 0, C-1

		while minRow <= maxRow and minCol <= maxCol:
			n = matrix[minRow][maxCol]
			if target > n:
				minRow += 1
			elif target < n:
				maxCol -= 1
			else:
				return True

		return False

M = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print Solution().searchMatrix(M, 5)
print Solution().searchMatrix(M, 30)