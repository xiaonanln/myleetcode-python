class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, b = None, None
        for i, n in enumerate(nums):
            if a and n == a[0]:
                a = (n, a[1]+1)
            elif b and n == b[0]:
                b = (n, b[1]+1)
            elif a is None: a = (n, 1)
            elif b is None: b = (n, 1)
            else:
                a = (a[0], a[1]-1)
                if a[1] == 0: a = None
                b = (b[0], b[1]-1)
                if b[1] == 0: b = None

        return [n for n in (a[0] if a else None, b[0] if b else None) if nums.count(n) > len(nums)//3]

print Solution().majorityElement([6,5,5])        