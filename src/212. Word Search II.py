

class TrieNode(object):
	__slots__ = ('children', 'isWord')
	def __init__(self):
		self.children = [None] * 26
		self.isWord = None

def trie_insert(root, word):
	for c in word:
		c = ord(c) - 97
		if root.children[c] is None:
			root.children[c] = TrieNode()

		root = root.children[c]

	root.isWord = word


class Solution(object):
	def findWords(self, board, words):
		"""
		:type board: List[List[str]]
		:type words: List[str]
		:rtype: List[str]
		"""
		trie = TrieNode()
		for w in words:
			trie_insert(trie, w)

		R = len(board)
		if not R:
			return []
		C = len(board[0])

		visited = [[False] * C for _ in xrange(R)]
		found = set()

		def bt(r, c, root):
			ch = ord(board[r][c]) - 97
			if root.children[ch] is None:
				# word not exists in trie
				return

			visited[r][c] = True
			root = root.children[ch]
			if root.isWord:
				found.add(root.isWord)

			for nr, nc in ( (r-1, c), (r+1, c), (r, c-1), (r, c+1) ):
				if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
					bt(nr, nc, root)
			visited[r][c] = False

		for r in xrange(R):
			for c in xrange(C):
				bt(r, c, trie)

		return list(found)

print Solution().findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], ["oath","pea","eat","rain"])
