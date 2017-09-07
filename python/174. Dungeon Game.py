class Solution(object):
	def calculateMinimumHP(self, dungeon):
		"""
		:type dungeon: List[List[int]]
		:rtype: int
		"""
		R = len(dungeon)
		C = len(dungeon[0])
		
		minBlood = [None] * C
		for r in xrange(R-1, -1, -1):
			for c in xrange(C-1, -1, -1):
				d = dungeon[r][c]
				if r < R-1 and c < C-1:
					minBlood[c] = min(max(1, minBlood[c] - d), max(1, minBlood[c+1] - d))
				elif r < R-1:
					minBlood[c] = max(1, minBlood[c] - d)
				elif c < C-1:
					minBlood[c] = max(1, minBlood[c+1] - d)
				else:
					minBlood[c] = 1-d if d<0 else 1

		return minBlood[0]