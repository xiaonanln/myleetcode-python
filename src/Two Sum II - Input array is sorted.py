class Solution(object):
	def twoSum(self, numbers, target):
		"""
		:type numbers: List[int]
		:type target: int
		:rtype: List[int]
		"""
		i, j = 0, len(numbers) - 1
		while i < j:
			sum = numbers[i] + numbers[j]
			if sum == target:
				return [i+1, j+1]
			elif sum < target:
				i += 1
			else:
				j -= 1


print Solution().twoSum([2, 7, 11, 15], 9)
