"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
"""

class Solution(object):
	def isAdditiveNumber(self, num):
		"""
		:type num: str
		:rtype: bool
		"""
		if len(num) < 3: return False
		MAXLEN = len(num) // 2 + 1
		# print 'MAXLEN', MAXLEN
		for l1i in xrange(1, MAXLEN+1):
			for l2i in xrange(1, MAXLEN+1):
				l1, l2 = l1i, l2i

				if l1 + l2 >= len(num): continue

				s = 0
				n1 = num[s:s+l1]
				n2 = num[s+l1:s+l1+l2]
				if (l1 > 1 and n1[0] == '0') or (l2 > 1 and n2[0] == '0'): continue

				while True:
					n3 = str(int(n1) + int(n2))
					l3 = len(n3)
					# print s, l1, l2, n1, n2, n3, num[s+l1+l2:s+l1+l2+l3] == n3, s+l1+l3 == len(num)
					if num[s+l1+l2:s+l1+l2+l3] != n3: break

					if s+l1+l2+l3 == len(num): return True
					s += l1
					l1, l2, n1, n2 = l2, l3, n2, n3

		return False

# print Solution().isAdditiveNumber("111")
print Solution().isAdditiveNumber("111122335588143")