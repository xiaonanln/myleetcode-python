import random
class Solution(object):

	def __init__(self, R, C):
		"""
		:type n_rows: int
		:type n_cols: int
		"""
		self.R, self.C = R, C
		self.zero_slots = []
		for r in xrange(R):
			for c in xrange(C):
				self.zero_slots.append((r, c))


	def flip(self):
		"""
		:rtype: List[int]
		"""
		i = random.randint(0, len(self.zero_slots)-1)
		ret = self.zero_slots[i]
		if i == len(self.zero_slots)-1:
			self.zero_slots.pop()
		else:
			self.zero_slots[i] = self.zero_slots.pop()
		return ret

	def reset(self):
		"""
		:rtype: void
		"""
		R, C = self.R, self.C
		self.zero_slots = []
		for r in xrange(R):
			for c in xrange(C):
				self.zero_slots.append((r, c))


# Your Solution object will be instantiated and called as such:
obj = Solution(3, 4)
print obj.flip()
obj.reset()