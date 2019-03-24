class Solution(object):
	def reachingPoints(self, sx, sy, tx, ty):
		"""
		:type sx: int
		:type sy: int
		:type tx: int
		:type ty: int
		:rtype: bool
		"""
		while True:
			print tx, ty, sx, sy
			if tx == sx and ty == sy:
				return True

			if tx < sx or ty < sy:
				return False

			if tx > ty:
				if tx == sx:
					return False
				tx, ty = tx - (tx - sx) // ty * ty, ty
				if tx > ty and tx != sx:
					tx -= ty
			elif ty > tx:
				if ty == sy:
					return False

				tx, ty = tx, ty - (ty - sy) // tx * tx
				if ty > tx and ty != sy:
					ty -= tx
			else: # ty == tx
				return False


assert Solution().reachingPoints(9, 10, 9, 19) == True
assert Solution().reachingPoints(10, 4, 10, 20) == False
assert Solution().reachingPoints(1, 5, 19, 5) == False