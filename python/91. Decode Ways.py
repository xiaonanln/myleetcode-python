class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s: return 0
		n, n1, n2 = 1, 0, 0
		for c in s:
			n, n1, n2 =  (
				n * (c > '0') + n1 + n2 * (c <= '6'),
				n * (c == '1'),
				n * (c == '2'),
			)
		return n

print Solution().numDecodings('12')