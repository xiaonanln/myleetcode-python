class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nums = sorted(str(_) for _ in xrange(1, n+1))
        return int(nums[k-1])

print Solution().findKthNumber(4289384, 1922239)