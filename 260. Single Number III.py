from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        C = Counter(nums)
        return [n for n, c in C.iteritems() if c == 1]


# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
print Solution().singleNumber([1, 2, 1, 3, 2, 5])
