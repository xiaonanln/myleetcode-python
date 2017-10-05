class Solution(object):
	def addStrings(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		i = len(num1) - 1
		j = len(num2) - 1
		c = 0

		res = []
		while i >= 0 or j >= 0 or c:
			v = (ord(num1[i]) - 48 if i >= 0 else 0) + (ord(num2[j]) - 48 if j >= 0 else 0) + c
			res.append(chr(v % 10 + 48))
			c = v >= 10
			i -= 1; j -= 1

		return ''.join(reversed(res))

print Solution().addStrings("111", "9")