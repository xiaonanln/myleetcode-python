class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        L, R = 0, len(A)
        while L < R:
            m = (L + R) // 2
            mv = A[m]
            if mv < target:
                L = m + 1
            elif mv > target:
                R = m
            else:
                return m
        
        return L
        

print Solution().searchInsert([1,3,5,6], 5)
print Solution().searchInsert([1,3,5,6], 2)
print Solution().searchInsert([1,3,5,6], 7)
print Solution().searchInsert([1,3,5,6], 0)