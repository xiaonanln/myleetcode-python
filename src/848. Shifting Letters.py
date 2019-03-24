class Solution(object):
	def shiftingLetters(self, S, shifts):
		"""
		:type S: str
		:type shifts: List[int]
		:rtype: str
		"""
		shift_accum = 0
		for i in xrange(len(shifts)-1, -1, -1):
			shift_accum, shifts[i] = shift_accum + shifts[i], shifts[i] + shift_accum

		return ''.join( chr((ord(c) - 97 + shifts[i]) % 26 + 97)  for i, c in enumerate(S))

assert Solution().shiftingLetters("abc", [3,5,9]) == 'rpl', Solution().shiftingLetters("abc", [3,5,9])
