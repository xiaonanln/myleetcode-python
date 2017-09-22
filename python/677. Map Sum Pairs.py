
class TrieNode(object):

	__slots__ = ('val', 'children')

	def __init__(self, val):
		self.val = val
		self.children = {}

	def set(self, s, val, idx):
		if idx < len(s):
			c = s[idx]
			if c not in self.children:
				self.children[c] = TrieNode(None)

			self.children[c].set( s, val, idx+1 )
		else:
			self.val = val

	def getNode(self, s, idx=0):
		if idx < len(s):
			c = s[idx]
			if c not in self.children:
				return None

			return self.children[c].getNode( s, idx+1 )
		else:
			return self

	def sumPrefix(self, prefix):
		node = self.getNode(prefix)
		if node is None:
			return 0

		def sum(node):
			# print 'sum', node, node.val
			v = 0
			if node.val is not None:
				v += node.val

			for c, child in node.children.iteritems():
				if child is None: continue
				v += sum(child)
			return v

		return sum(node)

class Trie(object):

	def __init__(self):
		self.root = TrieNode(None)

	def set(self, s, val):
		self.root.set(s, val, 0)

	def sumPrefix(self, prefix):
		return self.root.sumPrefix(prefix)

class MapSum(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.t = Trie()

	def insert(self, key, val):
		"""
		:type key: str
		:type val: int
		:rtype: void
		"""
		self.t.set(key, val)

	def sum(self, prefix):
		"""
		:type prefix: str
		:rtype: int
		"""
		return self.t.sumPrefix(prefix)

ms = MapSum()
ms.insert("apple", 3)
assert ms.sum("ap") == 3, ms.sum("ap")
ms.insert("app", 2)
assert ms.sum("ap") == 5, ms.sum("ap")