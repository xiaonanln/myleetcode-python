from collections import deque
class Solution(object):
	def minMutation(self, start, end, bank):
		"""
		:type start: str
		:type end: str
		:type bank: List[str]
		:rtype: int
		"""
		WL = len(start)
		bank = set(bank)
		bank = {w: i for i, w in enumerate(bank)}
		visited = [False] * len(bank)
		q = deque( [start] )
		dist = 0
		if end not in bank:
			return -1

		while q:
			qsize = len(q)
			dist += 1
			for _ in xrange(qsize):
				w = q.popleft()
				for i in xrange(0, WL):
					for c in 'ACGT':
						if c != w[i]:
							nw = w[:i] + c + w[i+1:]
							wi = bank.get(nw)
							# print nw, wi, visited
							if wi is None or visited[wi]: continue
							if nw == end:
								return dist

							visited[wi] = True
							q.append(nw)

		return -1

start = "AAAAACCC"
end =   "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
start = "AAAACCCC"
end = "CCCCCCCC"
bank = ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]
print Solution().minMutation( start, end, bank )