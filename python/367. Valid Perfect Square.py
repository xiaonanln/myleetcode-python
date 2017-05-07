class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num in (1, 4): return True 
        if num <= 4: return False 
        # now, num > 4
        i, j = 1, num
        while i <= j:
            print i, j
            m = (i+j) // 2
            mm = m*m
            if mm == num:
                return True 
            elif mm < num:
                i = m+1
            else: # mm > num
                j = m-1
                
        return False 
            