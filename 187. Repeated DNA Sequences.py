from collections import deque
class Solution(object):
	def findRepeatedDnaSequences(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		if len(s) <= 10: return []
		Q = deque(s[:10])
		visited = set( [s[:10]] )
		twice = set()

		# print  Q, visited

		for i in xrange(10, len(s)):
			Q.popleft()
			Q.append(s[i])
			v = ''.join(Q)
			# print v
			if v in visited:
				twice.add(v)
			else:
				visited.add(v)

		return list(twice)

print Solution().findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
print Solution().findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT') == ["AAAAACCCCC", "CCCCCAAAAA"]