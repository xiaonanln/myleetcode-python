class Solution(object):
	def anagramMappings(self, A, B):
		"""
		:type A: List[int]
		:type B: List[int]
		:rtype: List[int]
		"""
		poses = {}
		for i, n in enumerate(B):
			poses.setdefault(n, []).append( i )

		mapping = []
		for i, n in enumerate(A):
			mapping.append( poses[n].pop() )

		return mapping