class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		poses = [None] * 26
		for i, c in enumerate(s):
			c = ord(c)-97
			if poses[c] is None:
				poses[c] = i
			else:
				poses[c] = -1

		try: return min(p for p in poses if p >= 0)
		except ValueError: return -1

from collections import Counter
class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		indexes = {c:i for i, c in enumerate(s)}
		cc = Counter(s)
		try: return min(indexes[c] for c, n in cc.iteritems() if n == 1)
		except:return -1


print Solution().firstUniqChar('leetcode')
print Solution().firstUniqChar('loveleetcode')