TURN_LEFT = {
	(0, 1): (-1, 0),
	(-1, 0): (0, -1),
	(0, -1): (1, 0),
	(1, 0): (0, 1),
}

TURN_RIGTH = {
	v: k for k, v in TURN_LEFT.iteritems()
}

class Solution(object):
	def robotSim(self, commands, obstacles):
		"""
		:type commands: List[int]
		:type obstacles: List[List[int]]
		:rtype: int
		"""
		x, y = 0, 0
		dx, dy = 0, 1
		obstacles = {(_[0], _[1]) for _ in obstacles}
		maxdist = 0
		for c in commands:
			if c == -2:
				# turn left
				dx, dy = TURN_LEFT[(dx, dy)]
			elif c == -1:
				# turn right
				dx, dy = TURN_RIGTH[(dx, dy)]
			else:
				assert 1 <= c <= 9
				for _ in xrange(c):
					nx, ny = (x + dx, y + dy)
					if (nx, ny) not in obstacles:
						x, y = nx, ny
						maxdist = max(maxdist, (x*x)+(y*y))
					else:
						break

		return maxdist


assert Solution().robotSim([4, -1, 3], []) == 25

commands = [4,-1,4,-2,4]
obstacles = [[2,4]]
assert Solution().robotSim(commands, obstacles) == 65