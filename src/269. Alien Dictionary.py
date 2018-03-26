from itertools import izip, izip_longest
class Solution(object):
	def alienOrder(self, words):
		"""
		:type words: List[str]
		:rtype: str
		"""
		chars = [False] * 26
		adj = [[] for _ in xrange(26)] # the graph
		WN = len(words)
		for w in words:
			for c in w: chars[ord(c)-97] = 1

		for i in xrange(WN-1):
			w1 = words[i]
			w2 = words[i+1]

			for c1, c2 in izip(w1, w2):
				if c1 != c2: # first unsame char defines the ordder
					adj[ ord(c1)-97 ].append( ord(c2)-97 )
					break
			else: # no break, meaning c1 == c2 always
				if len(w1) > len(w2):
					return ''

		# do the toposort
		postOrder = []
		visited = [False] * 26
		instack = set()

		def dfs(u):
			visited[u] = True
			instack.add(u)

			for v in adj[u]:
				if chars[v]:
					if not visited[v]:
						if not dfs(v):
							return False
					elif v in instack:
						return False

			postOrder.append(u)
			instack.remove(u)
			return True

		for u in xrange(26):
			if chars[u] and not visited[u]:
				if not dfs(u):
					return ''

		print 'post order', postOrder, 'chars', chars
		return ''.join(chr(c+97) for c in reversed(postOrder))

# print Solution().alienOrder([
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ])
print `Solution().alienOrder(["wnlb"])`


