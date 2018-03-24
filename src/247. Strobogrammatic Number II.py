class Solution(object):
	def findStrobogrammatic(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		a = ['']
		b = ['0', '1', '8']
		if n == 0: return a
		elif n == 1: return b
		for l in xrange(2, n+1):
			# calculate for length i
			c = [x for s in a for x in ('0'+s+'0', '1'+s+'1', '8'+s+'8', '6'+s+'9', '9'+s+'6') ]
			a, b = b, c

		# the result is b
		return [x for x in b if x[0] != '0']


print Solution().findStrobogrammatic(0)
print Solution().findStrobogrammatic(1)
print Solution().findStrobogrammatic(2)
print Solution().findStrobogrammatic(3)
print Solution().findStrobogrammatic(4)