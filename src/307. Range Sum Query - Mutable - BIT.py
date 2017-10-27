
def lowbit(n):
	return (n ^ (n-1)) & n

class NumArray(object):
	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.N = len(nums)
		self.nums = [0] * self.N
		self.bit = [0] * (self.N + 1)
		for i, n in enumerate(nums):
			self.update(i, n)

	def update(self, i, val):
		"""
		:type i: int
		:type val: int
		:rtype: void
		"""
		diff = val - self.nums[i]
		self.nums[i] = val
		i += 1 # convert from index to BIT index
		while i <= self.N:
			self.bit[i] += diff
			i += lowbit(i)

	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		def sumTo(i):
			total = 0
			while i > 0:
				total += self.bit[i]
				i -= lowbit(i)
			return total

		i, j = i+1, j+1 # convert from index to BIT index
		return sumTo(j) - sumTo(i-1)


na = NumArray([1,3,5])
print na.sumRange(0, 2)
na.update(1, 2)
print na.sumRange(0, 2)