class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		R = len(matrix)
		if not R:
			return []

		C = len(matrix[0])
		res = []
		self.order1(matrix, res, 0, R-1, 0, C-1 )
		return res

	def order1(self, matrix, res, minR, maxR, minC, maxC):
		if minC > maxC: return
		for c in xrange(minC, maxC+1):
			res.append( matrix[minR][c] )

		self.order2(matrix, res,minR+1, maxR, minC, maxC)

	def order2(self, matrix, res, minR, maxR, minC, maxC):
		if minR > maxR: return
		for r in xrange(minR, maxR+1):
			res.append(matrix[r][maxC])
		self.order3(matrix, res,minR, maxR, minC, maxC-1)

	def order3(self, matrix, res, minR, maxR, minC, maxC):
		if minC > maxC:return
		for c in xrange(maxC, minC-1, -1):
			res.append( matrix[maxR][c] )

		self.order4(matrix, res,minR, maxR-1, minC, maxC)

	def order4(self, matrix, res, minR, maxR, minC, maxC):
		if minR > maxR: return
		for r in xrange(maxR, minR-1, -1):
			res.append(matrix[r][minC])
		self.order1(matrix, res,minR, maxR, minC+1, maxC)


print Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])