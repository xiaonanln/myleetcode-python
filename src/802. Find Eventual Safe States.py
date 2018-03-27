from collections import deque
class Solution(object):
	def eventualSafeNodes(self, graph):
		"""
		:type graph: List[List[int]]
		:rtype: List[int]
		"""
		# adj = graph
		N = len(graph)
		reverseGraph = [[] for _ in xrange(N)]
		for u, adj in enumerate(graph):
			for v in adj: # u -> v
				reverseGraph[v].append(u)

		safeNodes = deque([u for u, adj in enumerate(graph) if not adj])
		# print 'safe', safeNodes
		outdegree = [len(adj) for u, adj in enumerate(graph)]
		# print outdegree
		res = []
		while safeNodes:
			su = safeNodes.popleft()
			res.append(su)
			for sv in reverseGraph[su]: # reverse link: su -> sv, meaning sv -> su
				outdegree[sv] -= 1
				if outdegree[sv] == 0:
					safeNodes.append(sv)

		return res


print Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])
