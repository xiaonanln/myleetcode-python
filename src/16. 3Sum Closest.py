from bisect import bisect_left
class Solution(object):
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		nums.sort()
		L = len(nums)
		# print 'L', L
		S2 = []
		mins = float('inf')
		for i, n1 in enumerate(nums):
			if i >= L-2: continue
			if n1 + nums[-1] + nums[-2] < target and abs(target-(n1 + nums[-1] + nums[-2]))>=abs(mins-target):
				continue

			for j in xrange(i+1, L-1):
				n2 = nums[j]
				s2 = n1 + n2
				if s2 + nums[j+1] >= target and abs(s2 + nums[j+1]-target) >= abs(mins-target):
					continue

				# find target-sum in nums
				k = bisect_left(nums, target-s2, j+1)
				if k == L:
					k = L-1
				elif k > j+1:
					if abs(target-s2-nums[k-1]) < abs(target-s2-nums[k]):
						k -= 1

				s3 = s2 + nums[k]
				if abs(s3 - target) < abs(mins-target):
					mins = s3

		return mins

print Solution().threeSumClosest(

[0,5,10,-18,75,57,53,9,-89,19,-92,86,-14,-99,-63,-69,-21,62,-12,-3,93,-28,71,3,-64,34,39,-75,17,100,-64,-9,-75,-82,85,40,11,89,-39,-73,-81,91,-59,-39,-37,-89,-38,85,-68,-66,83,-62,6,-41,74,-81,-54,6,-35,21,-49,-72,39,-66,54,-25,69,97,-69,-87,-84,63,71,16,80,77,12,82,-36,24,10,-92,2,20,58,14,-40,79,79,-82,98,53,-4,-60,80,-96,0,0,74,40,-95,73,-64,78,-78,-66,-16,-84,-51,-27,60,-86],
-121

)