class Solution(object):
	def findDiagonalOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		R = len(matrix)
		if not R:
			return []

		C = len(matrix[0])

		r, c = 0, 0
		dir = 1 # dir can be (-1, 1) or (1, -1)
		res = [None] * (R*C)
		for i in xrange( R*C ):
			res[i] = matrix[r][c]

			# incr r, c to next position

			if dir == 1:
				if r == 0 or c == C-1:
					dir = -1
					if c < C-1:
						c += 1
					else:
						r += 1
				else:
					r += -1 * dir
					c += 1 * dir
			else:
				if c == 0 or r == R-1:
					dir = 1
					if r < R-1:
						r += 1
					else:
						c += 1
				else:
					r += -1 * dir
					c += 1 * dir

		return res

print Solution().findDiagonalOrder(
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
)
