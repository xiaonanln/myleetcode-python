class Solution(object):
	def rangeSumBST(self, root, L, R):
		if not root:
			return 0

		def calcsum(root):
			ret = 0
			if root.left and L < root.val:
				ret += calcsum(root.left)

			if L <= root.val <= R:
				ret += root.val

			if root.right and R > root.val:
				ret += calcsum(root.right)

			return ret

		return calcsum(root)