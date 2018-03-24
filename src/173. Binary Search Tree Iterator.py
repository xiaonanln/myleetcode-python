# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator_Generator(object):
	def __init__(self, root):
		"""
		:type root: TreeNode
		"""
		self.g = self.generator(root)
		self.nextVal = None

	def generator(self, root):
		if not root:
			return

		for val in self.generator(root.left):
			yield val

		yield root.val

		for val in self.generator(root.right):
			yield val

	def hasNext(self):
		"""
		:rtype: bool
		"""
		if self.nextVal is not None:
			return True

		try:
			self.nextVal = self.g.next()
			return True
		except StopIteration:
			return False

	def next(self):
		"""
		:rtype: int
		"""
		ret = self.nextVal
		self.nextVal = None
		return ret


class BSTIterator(object):
	def __init__(self, root):
		"""
		:type root: TreeNode
		"""
		self.stk = []
		p = root
		while p:
			self.stk.append(p)
			p = p.left

		if self.stk:
			self.cur = self.stk[-1]
		else:
			self.cur = None

	def hasNext(self):
		"""
		:rtype: bool
		"""
		# print 'hasNext', self.cur.val if self.cur else None, [node.val for node in self.stk]
		return self.cur is not None

	def next(self):
		"""
		:rtype: int
		"""
		assert self.cur

		val = self.cur.val
		# print 'next', val
		self.movetonext()
		return val

	def movetonext(self):
		cur = self.cur
		# print 'movetonext', cur, cur.right, self.stk
		if cur.right:
			cur = cur.right
			self.stk.append(cur)
			while cur.left:
				cur = cur.left
				self.stk.append(cur)
			# print 'cur', cur, self.stk
		else:

			self.stk.pop() # pop cur

			while True:
				if not self.stk:
					parent = None
					break

				parent = self.stk[-1]
				if parent.left == cur:
					break

				cur = parent
				self.stk.pop()

			# found parent with parent.left == cur
			cur = parent

		self.cur = cur
		if self.stk:
			assert self.cur == self.stk[-1]
		else:
			assert self.cur is None

		# print 'movetonext', cur


import utils
t = utils.maketree([1, None, 2])
it = BSTIterator(t)
while it.hasNext():
	print it.next()