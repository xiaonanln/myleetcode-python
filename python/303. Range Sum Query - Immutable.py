class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.accums = []
        accum = 0
        for n in nums:
            accum += n
            self.accums.append(accum)
        print self.accums 

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accums[j] -  self.accums[i-1] if i > 0 else self.accums[j]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)