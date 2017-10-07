
class TrieNode(object):
	__slots__ = ('children', 'isWord')
	def __init__(self):
		self.children = {}
		self.isWord = False

class Trie(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode()

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: void
		"""
		root = self.root
		for c in word:
			if c not in root.children:
				root.children[c] = TrieNode()

			root = root.children[c]

		root.isWord = True

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		root = self.root
		for c in word:
			root = root.children.get(c)
			if root is None:
				return False

		return root.isWord

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""

		root = self.root
		for c in prefix:
			root = root.children.get(c)
			if root is None:
				return False

		return True


