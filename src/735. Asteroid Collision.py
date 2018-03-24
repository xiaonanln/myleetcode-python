class Solution(object):
	def asteroidCollision(self, asteroids):
		"""
		:type asteroids: List[int]
		:rtype: List[int]
		"""
		stk = []
		for i, n in enumerate(asteroids):
			if n > 0:
				stk.append(n)
			else:
				while stk and 0 < stk[-1] < -n:
					stk.pop()

				if not stk or stk[-1] < 0:
					stk.append(n)
				elif stk[-1] == -n:
					stk.pop()

		return stk

		# maxpositive = -10000
		# remove = set()
		# for i, n in enumerate(asteroids):
		# 	if n > 0:
		# 		maxpositive = max(maxpositive, n)
		# 	else:
		# 		# n < 0
		# 		if -n <= maxpositive:
		# 			remove.add(i)
		# 		else:
		# 			maxpositive = -10000
		#
		# print remove
		# minnegative = 10000
		# for i, n in enumerate( reversed(asteroids) ):
		# 	# print i, n
		# 	if n < 0:
		# 		minnegative = min(minnegative, n)
		# 	else:
		# 		# n > 0
		# 		if -minnegative >= n:
		# 			remove.add(N-1-i)
		# 		else:
		# 			minnegative = 10000
		#
		# print remove
		# return [n for i, n in enumerate(asteroids) if i not in remove]

# print Solution().asteroidCollision([5, 10, -5])
# print Solution().asteroidCollision([8, -8])
# print Solution().asteroidCollision([10, 2, -5])
print Solution().asteroidCollision([-2,1,-1,-1])
print Solution().asteroidCollision([-2,-1,1,2])
