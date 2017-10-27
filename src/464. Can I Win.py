class Solution(object):
	def canIWin(self, maxChoosableInteger, desiredTotal):
		"""
		:type maxChoosableInteger: int
		:type desiredTotal: int
		:rtype: bool
		"""
		if desiredTotal > (1 + maxChoosableInteger) * maxChoosableInteger / 2:
			return False
		if maxChoosableInteger >= desiredTotal:
			return True

		mask = (1 << maxChoosableInteger) - 1
		# print '{0:b}'.format(mask)
		self.memo = [None] * (mask+1)
		return self.canIWinHelper( mask, desiredTotal )

	def canIWinHelper(self, mask, desiredTotal):
		# print 'canIWinHelper', mask, desiredTotal, self.memo[mask]
		if desiredTotal <= 0:
			return False

		if self.memo[mask] is not None:
			return self.memo[mask]

		b = 1
		n = 1
		canWin = False
		while b <= mask:
			if mask & b:
				submask = mask & ~b
				if not self.canIWinHelper(submask, desiredTotal-n):
					canWin = True
					break

			b = b << 1
			n += 1

		self.memo[mask] = canWin
		return canWin


print Solution().canIWin(10, 0)
print Solution().canIWin(20, 200)