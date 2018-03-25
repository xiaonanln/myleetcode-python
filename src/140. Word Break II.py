
class TrieNode(object):
	def __init__(self):
		self.children = {}
		self.isWord = False

	def addWord(self, w):
		self._addWord(w, 0, len(w))

	def _addWord(self, w, i, L):
		if i == L:
			self.isWord = True
		else:
			c = w[i]
			child = self.children.get(c)
			if child is None:
				child = self.children[c] = TrieNode()
			child._addWord(w, i+1, L)

class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""
		trieRoot = TrieNode()
		for w in wordDict:
			trieRoot.addWord(w)

		L = len(s)
		def getSentences(si):
			if si == L:
				return [ [] ]
			trieNode = trieRoot
			res = []
			for i in xrange(si, L):
				c = s[i]
				trieNode = trieNode.children.get(c)
				if trieNode is None:
					break

				if trieNode.isWord:
					sw = s[si:i+1]
					for _ in getSentences(i+1):
						res.append( [sw] + _ )
			return res

		return [ ' '.join(ws) for ws in getSentences(0)]

class Solution:

	# @param s, a string
	# @param dict, a set of string
	# @return a list of strings
	def wordBreak(self, s, dict):
		n = len(s)
		DP = [None] * (n + 1)
		DP[n] = [(n,)]  # DP[n] is set of all dividers

		for i in xrange(n - 1, -1, -1):
			dp = []
			for j in xrange(i + 1, n + 1):
				subs = s[i:j]
				if DP[j] and subs in dict:
					for _dp in DP[j]:
						dp.append((i,) + _dp)
			DP[i] = dp

		result = []
		for divs in DP[0]:
			sen = s[divs[0]:divs[1]]
			for i in xrange(1, len(divs) - 1):
				sen += ' '
				sen += s[divs[i]:divs[i + 1]]
			result.append(sen)

		return result

# s = "catsanddog"
# dict = ["cat", "cats", "and", "sand", "dog"]
# print Solution().wordBreak(s, dict)
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print Solution().wordBreak(s, dict)