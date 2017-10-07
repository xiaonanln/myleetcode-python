class Solution(object):
	def computeArea(self, A, B, C, D, E, F, G, H):
		"""
		:type A: int
		:type B: int
		:type C: int
		:type D: int
		:type E: int
		:type F: int
		:type G: int
		:type H: int
		:rtype: int
		"""
		return (C-A) * (D-B) + (G-E) * (H-F) - max(0, min(C, G) - max(A, E)) * max(0, min(D, H) - max(B, F))