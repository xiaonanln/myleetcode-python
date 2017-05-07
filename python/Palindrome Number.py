class Solution1: # Accepted
    # @return a boolean 
    def isPalindrome(self, x):
        if x < 0: return False
        
        smallDiv = 1
        bigDiv = 1
        while bigDiv * 10 <= x:
            bigDiv *= 10
        
        while bigDiv > 1:
            bigd = x // bigDiv
            smalld = x % 10
            
#             print bigDiv, smallDiv, bigd, smalld
            
            if bigd != smalld: return False
        
            x = x % bigDiv
            x = x // 10
        
            bigDiv //= 100
            smallDiv *= 10
        
        return True
    
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        l = list(str(x))
        return l == list(reversed(l))
    
# print Solution().isPalindrome(232)
print Solution1().isPalindrome(1001)
print Solution1().isPalindrome(-232)