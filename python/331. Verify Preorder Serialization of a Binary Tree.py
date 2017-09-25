class Solution(object):
	def isValidSerialization(self, preorder):
		"""
		:type preorder: str
		:rtype: bool
		"""
		preorder = preorder.split(',')
		isValid, j = self.expectValidTree(preorder, 0)
		return isValid and j == len(preorder)

	def expectValidTree(self, preorder, i):
		if i >= len(preorder): return False, i
		if preorder[i] == '#': return True, i+1
		ok, j = self.expectValidTree(preorder, i+1)
		if not ok: return False, j
		ok, j = self.expectValidTree(preorder, j)
		return ok, j

print Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
print Solution().isValidSerialization("1,#")
print Solution().isValidSerialization("9,#,#,1")
