class Solution(object):
    def __init__(self):
        self.visited = set()
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while True:
            # print 'check', n
            if n == 1: return True 
            if n in self.visited: return False 
            self.visited.add(n)

            s = 0
            while n > 0:
                n, d = divmod(n, 10)
                s += d * d
            
            n = s

# print Solution().isHappy(19)        
print Solution().isHappy(25)