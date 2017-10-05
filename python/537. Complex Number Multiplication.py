class Solution(object):
	def complexNumberMultiply(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		aa, ab = a[:-1].split('+')
		ba, bb = b[:-1].split('+')
		aa, ab, ba, bb = int(aa), int(ab), int(ba), int(bb)
		x, y = aa*ba-ab*bb, aa*bb+ab*ba
		return '%d+%di' % (x, y)