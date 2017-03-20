class SolutionEasy(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return target in {num for row in matrix for num in row}

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False 

        R = len(matrix) # number of rows
        C = len(matrix[0]) # number of cols

        i, j = 0, R*C-1

        while i <= j:
        	mid = (i+j) // 2
        	v = matrix[ mid//C ][mid%C]
        	if v == target:
        		return True 
        	elif target < v:
        		j = mid-1
        	else: # target > v
        		i = mid+1

        return False 
        
print Solution().searchMatrix(
	[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3
	)