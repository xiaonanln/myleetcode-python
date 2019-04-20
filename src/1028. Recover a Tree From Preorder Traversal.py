# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def recoverFromPreorder(self, S):
		"""
		:type S: str
		:rtype: TreeNode
		"""
		i = 0
		L = len(S)

		nodestack = []
		while i < L:
			depth = 0
			while i < L and S[i] == '-':
				depth += 1
				i += 1

			num = ''
			while i < L and '0' <= S[i] <= '9':
				num += S[i]
				i += 1

			num = int(num)
			# print depth, num
			node = TreeNode(num)
			if not nodestack:
				assert depth == 0
				nodestack.append(node)
			else:
				lastnode = nodestack[-1]
				assert 0 < depth <= len(nodestack)
				isLeftChild = True
				while len(nodestack) > depth:
					isLeftChild = False
					nodestack.pop()

				if isLeftChild:
					nodestack[-1].left = node
				else:
					nodestack[-1].right = node
				nodestack.append(node)

		return nodestack[0]


print Solution().recoverFromPreorder("1-2--3--4-5--6--7")
