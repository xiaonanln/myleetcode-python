class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        last = None
        writep = 0
        cur = 0
        while cur < len(A):
            if A[cur] != last:
                A[writep] = A[cur]
                last = A[writep]
                writep += 1
            else:
                pass
            
            cur += 1
        
        return writep
    
A = [1,1,2]
print Solution().removeDuplicates(A)
print A

A = []
print Solution().removeDuplicates(A)
print A

A = [1]
print Solution().removeDuplicates(A)
print A