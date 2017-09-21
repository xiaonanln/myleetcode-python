class Solution(object):
	def __init__(self):
		self.dp = [1]

	def findIntegers(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		if num <= 0:
			return 1
		d = 1
		nd = 1
		self.dp.append(2)

		while (d << 1) <= num:
			d <<= 1
			nd += 1
			self.dp.append( self.dp[nd-1] + self.dp[nd-2] )

		# print self.dp
		return self.dp[nd-1] + self.findIntegersHelper( d >> 2, nd-2, num - d )

	def findIntegersHelper(self, d, nd, num):
		print 'find', d, nd, num
		# assert num < d * 2, (num, d*2)
		if num <= 0: return 1
		elif num >= d*2 - 1:
			return self.dp[nd]

		# if d <= 0:
		# 	return 1

		if num >= d:
			res = self.dp[nd-1] + self.findIntegersHelper(d >> 2, nd-2, num - d)
		else:
			res = self.findIntegersHelper(d>>1, nd-1, num)
		return res

print Solution().findIntegers(0)
print Solution().findIntegers(1)
print Solution().findIntegers(5)
print Solution().findIntegers(999999999)