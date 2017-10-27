class Solution(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		R = len(matrix)
		if not R: return
		C = len(matrix[0])

		clearR0, clearC0 = False, False
		for r in xrange(R):
			for c in xrange(C):
				if matrix[r][c] == 0:
					if r == 0:
						clearR0 = True
					else:
						matrix[r][0] = 0

					if c == 0:
						clearC0 = True
					else:
						matrix[0][c] = 0

		for r in xrange(1, R):
			if matrix[r][0] == 0:
				matrix[r][:] = [0] * C
		for c in xrange(1, C):
			if matrix[0][c] == 0:
				for r in xrange(R):
					matrix[r][c] = 0

		if clearR0:
			matrix[0][:] = [0] * C

		if clearC0:
			for r in xrange(R):
				matrix[r][0] = 0
