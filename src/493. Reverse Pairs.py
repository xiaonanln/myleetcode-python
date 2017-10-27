

class MergeSort(object):
	def __init__(self, list):
		self.list = list
		self.numReversePairs = 0

	def sort(self):
		aux = [0 for _ in self.list]
		self.mergesort(self.list, 0, len(self.list), aux)

	def mergesort(self, list, l, h, aux):
		if h <= l+1:
			return

		mid = (l+h)//2
		self.mergesort(list, l, mid, aux)
		self.mergesort(list, mid, h, aux)
		self.merge(list, l, mid, h, aux)

	def merge(self, list, l, m, h, aux):
		aux[l:h] = list[l:h] # copy all items to aux

		r1 = l
		for r2 in xrange(m, h):
			while r1 < m and list[r1] <= list[r2] * 2:
				r1 += 1

			if r1 == m: break
			self.numReversePairs +=  (m-r1)

		w = l
		r1, r2 = l, m
		while r1 < m and r2 < h:
			if aux[r1] <= aux[r2]:
				list[w] = aux[r1]
				r1 += 1
			else:
				list[w] = aux[r2]
				r2 += 1

			w += 1

		while r1 < m:
			list[w] = aux[r1]
			w += 1
			r1 += 1


class Solution(object):
	def reversePairs(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		M = MergeSort(nums)
		M.sort()
		return M.numReversePairs


print Solution().reversePairs([1,3,2,3,1])
print Solution().reversePairs([2,4,3,5,1])