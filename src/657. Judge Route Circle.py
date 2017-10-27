from collections import Counter
class Solution(object):
	def judgeCircle(self, moves):
		"""
		:type moves: str
		:rtype: bool
		"""
		C =  Counter(moves)
		return C['L'] == C['R'] and C['U'] == C['D']


class Solution(object):
	def judgeCircle(self, moves):
		"""
		:type moves: str
		:rtype: bool
		"""

		x, y = 0, 0
		for c in moves:
			if c == 'L':
				x -= 1
			elif c == 'R':
				x += 1
			elif c == 'U':
				y -= 1
			elif c == 'D':
				y += 1

		return x == 0 and y == 0