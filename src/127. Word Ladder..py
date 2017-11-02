from collections import deque
from string import lowercase as chars
class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: int
		"""
		wordList = set(wordList)
		if endWord not in wordList:
			return 0

		WL = len(endWord)
		q = deque([endWord])
		steps = 1
		while q:
			steps += 1
			qlen = len(q)
			for _ in xrange(qlen):
				w = q.popleft()
				for i in xrange(WL):
					for c in chars:
						if w[i] == c: continue
						nw = w[:i] + c + w[i+1:]
						if nw == beginWord:
							return steps
						elif nw in wordList:
							q.append(nw)
							wordList.remove(nw)

		return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print Solution().ladderLength(beginWord, endWord, wordList)