
class UF(object):
	def __init__(self, N):
		self.list = [i for i in xrange(N+1)] # every V points to self

	def connect(self, u, v):
		id1 = self.id(u)
		id2 = self.id(v)
		self.list[id2] = id1

	def id(self, v):
		pv = self.list[v]
		if pv == v:
			return v

		res = self.list[v] = self.id(pv)
		return res

class Solution(object):
	def findRedundantConnection(self, edges):
		"""
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		N = max(v for u, v in edges)
		# print 'N', N

		uf = UF(N)
		for u, v in edges:
			if uf.id(u) != uf.id(v):
				uf.connect(u, v)
			else:
				return [u, v]

print Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])
print Solution().findRedundantConnection([[1,2], [1,3], [2,3]])

