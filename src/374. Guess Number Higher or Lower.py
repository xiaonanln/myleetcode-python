# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(num):
	if num < 6: return 1
	elif num > 6: return -1
	else: return 0

class Solution(object):
	def guessNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		i, j = 1, n
		while i <= j:
			m = (i + j) // 2
			g = guess(m)
			# print i, j,m, g

			if g == 0:
				return m
			elif g == -1:  # m < real
				j = m - 1
			else:  # g == 1, m > real
				i = m + 1




print Solution().guessNumber(10)