class Solution(object):
	def countSmaller(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		N = len(nums)
		nums = [(n, i) for i, n in enumerate(nums)]
		# print nums
		aux = [None] * N

		self.moveRight = [0] * N
		self.mergeSort(nums, 0, N-1, aux)
		# print nums
		return self.moveRight

	def mergeSort(self, nums, i, j, aux):
		if i>=j:
			return
		m = (i+j) // 2
		self.mergeSort(nums, i, m, aux)
		self.mergeSort(nums, m+1, j, aux)
		# print 'merge', i, m, m+1, j

		# merge i:m and m+1:j
		aux[i:j+1] = nums[i:j+1]
		wi, r1, r2 = i, i, m+1

		while r1 <= m and r2 <= j:
			if aux[r1] <= aux[r2]:
				nums[wi] = aux[r1]
				if r1 < wi:
					self.moveRight[aux[r1][1]] += (wi-r1)

				r1 += 1
			else:
				nums[wi] = aux[r2]
				if r2 < wi:
					self.moveRight[aux[r2][1]] += (wi-r2)
				r2 += 1
			wi += 1

		while r1 <= m:
			nums[wi] = aux[r1]
			if r1 < wi:
				self.moveRight[aux[r1][1]] += (wi-r1)
			r1 += 1
			wi += 1

print Solution().countSmaller([5, 2, 6, 1])