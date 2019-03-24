M = 10**9 + 7
class Solution(object):
	def checkRecord(self, n):
		if n == 0:
			return 1

		P, AP, L, LL, AL, ALL, A = 1, 0, 1, 0, 0, 0, 1

		for i in xrange(2, n+1):
			P, AP, L, LL, AL, ALL, A = (
				(P+L+LL)%M,
				(AP+AL+ALL+A)%M,
				P,
				L,
				(AP+A)%M,
				AL,
				(P + L + LL)%M,
			)

		return (P + AP + L + LL + AL + ALL + A) % M

assert Solution().checkRecord(0) == 1
assert Solution().checkRecord(1) == 3
assert Solution().checkRecord(2) == 8
assert Solution().checkRecord(3) == 19