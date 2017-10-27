# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None`


#         self.right = None
#         self.next = None

from collections import deque
class Solution: # O(n) space
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		if not root: return
		q = deque([root])
		levelsize = 1
		while q:
			lastnode = None
			for i in xrange(levelsize):
				node = q.popleft()
				if lastnode is not None:
					lastnode.next = node
				lastnode = node

				if node.left:
					q.append(node.left)
					q.append(node.right)

			levelsize <<= 1

class Solution: # O(1) space
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		while root and root.left:
			p = root
			while p:
				p.left.next = p.right
				p.right.next = p.next and p.next.left
				p = p.next

			root = root.left


