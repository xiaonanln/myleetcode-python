class Solution(object):
	def frequencySort(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		freq = [0] * 256
		for c in s:
			freq[ord(c)] += 1

		return ''.join(chr(c) for n, c in sorted([(n, c) for c, n in enumerate(freq)], reverse = True) for _ in xrange(n))


print Solution().frequencySort("acacac")
print Solution().frequencySort("abcddd")