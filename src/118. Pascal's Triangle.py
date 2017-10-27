class Solution(object):
	def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		lastRow = []
		res = []
		for r in xrange(numRows):
			row = []

			for i in xrange( r+1 ):
				if i == 0 or i == r:
					row.append(1)
				else:
					row.append( lastRow[i-1] + lastRow[i] )
			res.append(row)
			lastRow = row
		return res

for r in Solution().generate(5):
	print r