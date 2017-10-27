from itertools import izip
class Solution(object):
	def getHint(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		A, B = 0, 0
		cs, cg = [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]
		for sc, gc in izip(secret, guess):
			if sc == gc:
				A += 1
			cs[ord(sc)-48] += 1
			cg[ord(gc)-48] += 1

		for c1, c2 in izip(cs, cg):
			B += min(c1, c2)
		B -= A

		return str(A) + 'A' + str(B) + 'B'

print Solution().getHint('1807', '7810')
print Solution().getHint('1123', '0111')