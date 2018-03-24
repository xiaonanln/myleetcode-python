class Solution(object):
	def countBinarySubstrings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0

		counts = []
		lastc = None
		num = 0
		for c in s:
			if c == lastc:
				num += 1
			else:
				counts.append(num)
				lastc = c
				num = 1

		if num:
			counts.append(num)
		res = 0
		for i in xrange(1, len(counts)):
			res += min(counts[i], counts[i-1])

		return res

print Solution().countBinarySubstrings("11")
print Solution().countBinarySubstrings("11001100")
