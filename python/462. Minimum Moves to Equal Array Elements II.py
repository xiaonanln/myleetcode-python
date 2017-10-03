from collections import Counter
class Solution(object): # bad solution
	def minMoves2(self, _nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not _nums: return 0

		C = Counter(_nums)
		nums = C.items()
		nums.sort()

		prevTarget = nums[0][0] - 1
		moves = minMoves = sum((n - prevTarget) * c for n, c in nums)
		equalNums = 0; prevNums = 0; postNums = len(_nums)
		# print prevTarget, minMoves, prevNums, postNums
		for target, count in nums:
			# let num be new target, recalculate minMoves
			moves = moves + (prevNums + equalNums - postNums) * (target - prevTarget)
			minMoves = min(minMoves, moves)

			prevTarget, equalNums, prevNums, postNums = target, count, prevNums+equalNums, postNums-count

		return minMoves

print Solution().minMoves2([1,2,3])