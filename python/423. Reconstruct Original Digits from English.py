from collections import Counter
class Solution(object):
	def originalDigits(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		C = Counter(s)
		C2 = [0] * 10
		if C['x']: # get six
			n = C['x']
			C2[6] = n
			C['s'] -= n
			C['i'] -= n
			C['x'] -= n

		if C['z']: # get zero
			n = C['z']
			C2[0] = n
			C['z'] -= n
			C['e'] -= n
			C['r'] -= n
			C['o'] -= n

		if C['w']:  # get two
			n = C['w']
			C2[2] = n
			C['t'] -= n
			C['w'] -= n
			C['o'] -= n

		if C['u']:  # get 4
			n = C['u']
			C2[4] = n
			C['f'] -= n
			C['o'] -= n
			C['u'] -= n
			C['r'] -= n

		if C['f']:  # get 5
			n = C['f']
			C2[5] = n
			C['f'] -= n
			C['i'] -= n
			C['v'] -= n
			C['e'] -= n

		if C['v']:  # get 7
			n = C['v']
			C2[7] = n
			C['s'] -= n
			C['e'] -= n
			C['v'] -= n
			C['e'] -= n
			C['n'] -= n

		if C['g']:  # get 8
			n = C['g']
			C2[8] = n
			C['e'] -= n
			C['i'] -= n
			C['g'] -= n
			C['h'] -= n
			C['t'] -= n

		if C['i']:  # get 9
			n = C['i']
			C2[9] = n
			C['n'] -= n
			C['i'] -= n
			C['n'] -= n
			C['e'] -= n

		if C['h']:  # get 9
			n = C['h']
			C2[3] = n
			C['t'] -= n
			C['h'] -= n
			C['r'] -= n
			C['e'] -= n
			C['e'] -= n

		if C['o']:  # get one
			n = C['o']
			C2[1] = n
			C['o'] -= n
			C['n'] -= n
			C['e'] -= n

		# print C2
		return ''.join(str(n) for n, c in enumerate(C2) for _ in xrange(c))

print Solution().originalDigits("otw")
# print Solution().originalDigits("fviefuro")
