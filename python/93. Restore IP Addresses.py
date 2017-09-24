class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		dots = [0, -1, -1, -1]
		L = len(s)
		res = []
		def bt(pos):
			leftDots = 4 - pos
			if L - dots[pos-1] > 3 + leftDots * 3:
				return
			elif L - dots[pos-1] < 1+leftDots:
				return

			if pos == 4:
				# print s, dots
				res.append( s[0:dots[1]] +'.'+s[dots[1]:dots[2]]+'.' + s[dots[2]:dots[3]]+'.' + s[dots[3]:] )
				return

			pi = dots[pos-1]
			for i in (pi+1, pi+2, pi+3) if s[pi] != '0' else (pi+1, ):
				v = int(s[pi:i])
				if v > 255: continue

				if pos == 3: # last pos
					v2 = s[i:]
					if not v2 or int(v2) > 255: continue
					if v2 != '0' and v2[0] == '0': continue

				dots[pos] = i
				bt(pos+1)

		bt(1)
		return res

print Solution().restoreIpAddresses("010010")
# print Solution().restoreIpAddresses("25525511135")