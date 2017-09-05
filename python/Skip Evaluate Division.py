from itertools import izip
class Solution(object):
	def calcEquation(self, equations, values, queries):
		"""
		:type equations: List[List[str]]
		:type values: List[float]
		:type queries: List[List[str]]
		:rtype: List[float]
		"""
		sid = {}
		N = 0
		for x, y in equations:
			if x not in sid:
				sid[x] = N
				N += 1

			if y not in sid:
				sid[y] = N
				N += 1

		# print sid, N
		graphEdges = [[] for _ in xrange(N)]
		for (x, y), val in izip(equations, values):
			x, y = sid[x], sid[y]
			graphEdges[x].append( (y, val) )
			graphEdges[y].append( (x, 1.0/val) )

		# print graphEdges
		marked = [False] * N
		com = [-1] * N
		comcount = 0
		vals = [None] * N

		def dfs(x, val):
			marked[x] = True
			vals[x] = val
			com[x] = comcount

			for y, yv in graphEdges[x]:
				if not marked[y]:
					dfs(y, val / yv)

		for x in xrange(N):
			if not marked[x]:
				dfs(x, 1.0)
				comcount += 1

		# print marked
		# print com
		# print vals
		# print comcount

		res = []
		for x, y in queries:
			if x not in sid or y not in sid:
				res.append(-1.0)
				continue

			x, y = sid[x], sid[y]

			if com[x] != com[y]:
				res.append(-1.0)
				continue

			res.append(vals[x] / vals[y])

		return res

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print Solution().calcEquation( equations, values, queries )