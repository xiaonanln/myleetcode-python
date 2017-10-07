class Solution(object):
	def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""

		i = len(a)-1
		j = len(b)-1

		c = 0
		res  = ''
		while i >= 0 or j >= 0 or c:
			v = (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0) + c
			res = str(v % 2) + res
			c = v >= 2

			if i >= 0: i -= 1
			if j >= 0: j -= 1

		return res

print Solution().addBinary("11", "1")