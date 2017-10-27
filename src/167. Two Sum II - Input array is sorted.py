class Solution(object):
	def twoSum(self, numbers, target):
		"""
		:type numbers: List[int]
		:type target: int
		:rtype: List[int]
		"""
		i, j = 0, len(numbers)-1
		while i < j:
			v = numbers[i] + numbers[j]
			if target < v:
				j -= 1
			elif target > v:
				i += 1
			else:
				return [i+1, j+1]


print Solution().twoSum([2,7,11,15], 9)