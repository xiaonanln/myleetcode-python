# file encoding: utf8

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
    	resultS = None
    	
    	R = []
    	S = 0
    	for n in A:
    		if S < 0:
    			R = []
    			S = 0
    			
        	S += n
        	R.append(n)
        	if resultS is None or resultS < S:
        		resultS = S
        
        return resultS
        	
        	
       
S = Solution()
print S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
