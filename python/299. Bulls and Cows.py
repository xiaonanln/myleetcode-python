from collections import Counter
class Solution(object):
	def getHint(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		bulls = 0
		unmatch1, unmatch2 = Counter(), Counter()
		for c1, c2 in zip(secret, guess):
			if c1 == c2: bulls += 1
			else:
				unmatch1[c1] += 1
				unmatch2[c2] += 1

		cows = 0
		for n in set( unmatch1.keys() + unmatch2.keys() ):
			cows += min(unmatch1[n], unmatch2[n])
			
		return '%dA%dB' % (bulls, cows)

print Solution().getHint("1807", "7810")
print Solution().getHint("1123", "0111")