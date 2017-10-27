class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0

        D = [None] * len(nums)
        D[0] = 1
        for i in xrange(1, len(nums)):
        	n = nums[i]
        	maxlen = 1

        	for j in xrange(0, i):
        		if nums[j] < n:
        			maxlen = max(maxlen, D[j] + 1)

        	D[i] = maxlen

        return max(D)

print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
