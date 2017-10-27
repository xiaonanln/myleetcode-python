class Solution(object):
	def isNumber(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		s = s.strip()
		dot = False
		e = False
		justE = False
		justDot = False
		anyDigit = False
		expectSign = '+-'
		for c in s:
			if c in expectSign:
				expectSign = ''
				continue

			expectSign = ''
			if c == '.':
				if e or dot or justE: return False
				else:
					justDot = dot = True

			elif c == 'e':
				if e or not anyDigit: return False
				e = True
				justE = True
				expectSign = '-+'
			elif '0' <= c <= '9':
				justE = False
				justDot = False
				anyDigit = True
				continue
			else:
				return False

		return not justE and anyDigit

# assert Solution().isNumber("0") == True
# assert Solution().isNumber(" 0.1 ") == True
# assert Solution().isNumber("abc") == False
# assert Solution().isNumber("1 a") == False
# assert Solution().isNumber("2e10") == True
# assert Solution().isNumber("e") == False
# assert Solution().isNumber(".") == False
assert Solution().isNumber(" 005047e+6") == True
