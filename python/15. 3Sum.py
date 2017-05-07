

class SlowSolution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = set()
		N = len(nums)
		for i in xrange(N-2):
			for j in xrange(i+1, N-1):
				for k in xrange(j+1, N):
					if nums[i] + nums[j] + nums[k] == 0:
						res.add( tuple(sorted([nums[i], nums[j], nums[k]])) )
		return list(res)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        for i in xrange(N-1)
        print len(nums)


print SlowSolution().threeSum([-1, 0, 1, 2, -1, -4])
print SlowSolution().threeSum([13,-14,-10,-4,4,4,0,-14,5,-9,-3,-10,14,7,-3,-4,-3,12,-14,2,-11,-6,0,-7,13,-2,-7,-11,-14,-13,5,14,-12,11,-13,-1,-8,2,0,4,1,4,10,-8,-11,-8,3,1,11,4,-12,8,5,-4,-14,-4,9,-13,-8,2,-11,12,-7,14,0,-5,-2,7,5,5,-3,13,-6,-8,-10,-10,-9,0,6,-12,11,2,11,1,13,4,12,-1,6,-11,-14,2,9,-6,1,-6,-4,14,-13,8,4,-1,6,6,-2,11,11,4,-4,-5,-1,-8,12,-13,1,10,7,-10,-14,-10,-5,-13,0,11])

print Solution().threeSum([-1, 0, 1, 2, -1, -4])
print Solution().threeSum([13,-14,-10,-4,4,4,0,-14,5,-9,-3,-10,14,7,-3,-4,-3,12,-14,2,-11,-6,0,-7,13,-2,-7,-11,-14,-13,5,14,-12,11,-13,-1,-8,2,0,4,1,4,10,-8,-11,-8,3,1,11,4,-12,8,5,-4,-14,-4,9,-13,-8,2,-11,12,-7,14,0,-5,-2,7,5,5,-3,13,-6,-8,-10,-10,-9,0,6,-12,11,2,11,1,13,4,12,-1,6,-11,-14,2,9,-6,1,-6,-4,14,-13,8,4,-1,6,6,-2,11,11,4,-4,-5,-1,-8,12,-13,1,10,7,-10,-14,-10,-5,-13,0,11])