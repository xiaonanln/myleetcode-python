class Solution(object):
	def partitionLabels(self, S):
		"""
		:type S: str
		:rtype: List[int]
		"""
		N = len(S)
		leftchars = [0] * (N + 1)
		for i in xrange(N - 1, -1, -1):
			leftchars[i] = leftchars[i + 1] | (1 << (ord(S[i]) - 97))

		ret = []
		ss_start = 0
		i = 0
		while i < N:
			ss = 0
			ss |= (1 << (ord(S[i]) - 97))
			i += 1
			while ss & leftchars[i] != 0:
				# include the next char
				ss |= (1 << (ord(S[i]) - 97))
				i += 1

			ret.append(i - ss_start)
			ss_start = i

		return ret


print Solution().partitionLabels("ababcbacadefegdehijhklij")
