
class TreeNode(object):
	def __init__(self, i, j, index, val):
		self.i, self.j = i, j
		self.index = index
		self.total = self.val = val
		self.left = self.right = None
		self.parent = None

	def __str__(self):
		return 'TN[%d-%d-%d]%d/%d' % (self.i, self.index, self.j, self.val,self.total)

class NumArray(object):
	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		def buildTree(i,j):
			if i > j: return None

			m = (i+j) // 2
			root = TreeNode(i, j, m, nums[m])
			root.left = buildTree(i, m-1)
			root.right = buildTree(m+1, j)
			if root.left: root.left.parent = root
			if root.right: root.right.parent= root

			root.total += (root.left.total if root.left else 0) + (root.right.total if root.right else 0)
			return root

		self.tree = buildTree(0, len(nums)-1)

	def update(self, i, val):
		"""
		:type i: int
		:type val: int
		:rtype: void
		"""
		def updateHelper(root, i, val):
			if root.index == i:
				diff = val - root.val
				root.val = val
				while root:
					root.total += diff
					root = root.parent
			elif i < root.index:
				updateHelper(root.left, i, val)
			else:
				updateHelper(root.right, i, val)

		updateHelper(self.tree, i, val)

	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		def sumRangeHelper(root, i, j):
			# print 'sumRangeHelper', root
			if not root or root.i > j or root.j < i: # not in i, j
				return 0
			elif root.i >= i and root.j <= j: # fully in i, j
				return root.total

			return sumRangeHelper(root.left, i, j) + (root.val if i<=root.index<=j else 0) + sumRangeHelper(root.right, i, j)

		return sumRangeHelper(self.tree, i, j)

na = NumArray([1,3,5])
print na.sumRange(0, 2)
na.update(1, 2)
print na.sumRange(0, 2)