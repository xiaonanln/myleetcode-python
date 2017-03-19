class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        l, r = 0, len(A) - 1
        hit = None
        while l <= r:
            m = (l + r) // 2
            v = A[m]
            if v < target:
                l = m + 1
            elif v > target:
                r = m - 1
            else: # if v == target
                hit = m
                break 
            
#         print A, (l, A[l] if l < len(A) else None), (r, A[r] if r >= 0 else None), target, hit
        
        if hit is None: 
            return [-1, -1]
        else:
            return [self.findLeftMost(A, l, hit, target), self.findRightMost(A, hit+1, r+1, target) - 1]
        
    def findLeftMost(self, A, s, e, target):
        while s < e:
            m = (s + e) // 2
            v = A[m]
            assert v <= target
            if v < target:
                s = m + 1
            else: # v == target
                e = m
            
        return s
    
    def findRightMost(self, A, s, e, target):
        while s < e:
            m = (s + e) // 2
            v = A[m]
            assert v >= target
            if v > target:
                e = m
            else:
                s = m + 1
        return s

        
            
# print Solution().searchRange([], 2)
# print Solution().searchRange([1], 2)
# print Solution().searchRange([1,2, 3], 1)
print Solution().searchRange([1], 1)    
# print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)