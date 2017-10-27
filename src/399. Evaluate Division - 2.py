
from itertools import izip
from collections import deque

class Solution(object):
	def calcEquation(self, equations, values, queries):
		"""
		:type equations: List[List[str]]
		:type values: List[float]
		:type queries: List[List[str]]
		:rtype: List[float]
		"""
		vertex = {}
		for a, b in equations:
			if a not in vertex: vertex[a] = len(vertex)
			if b not in vertex: vertex[b] = len(vertex)
		print 'vertex', vertex
		V = len(vertex)
		adjs = [[] for _ in xrange(V)]

		for (a, b), val in izip(equations, values):
			a, b = vertex[a], vertex[b]
			adjs[a].append((b, val))
			adjs[b].append((a, 1.0/val))

		component = [-1] * V
		vals = [None] * V
		componentId = 0

		def bfs(v):
			q = deque()
			q.append(v)
			component[v] = componentId
			vals[v] = 1.0
			while q:
				v = q.popleft()

				for vv, div in adjs[v]:
					if component[vv] == -1:
						component[vv] = componentId
						vals[vv] = vals[v] / div
						q.append(vv)

		for v in xrange(V):
			if component[v] == -1:
				bfs(v)
				componentId += 1

		def calcQuery(a, b):
			if a not in vertex or b not in vertex:
				return -1.0
			a = vertex[a]; b = vertex[b]
			if component[a] != component[b]: return -1.0

			return vals[a] / vals[b]

		return [calcQuery(a, b) for a, b in queries]

print Solution().calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])
