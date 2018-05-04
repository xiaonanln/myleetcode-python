class Solution:
	def countBits(self, num):
		"""
		:type num: int
		:rtype: List[int]
		"""
		p = 1
		res = [0] * (num+1)
		for n in range(1, num+1):
			while (p << 1) <= n:
				p <<= 1

			# assert p <= n
			res[n] = res[n-p] + 1

		return res



print(Solution().countBits(5))