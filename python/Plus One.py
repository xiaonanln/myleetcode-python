class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        C = 1
        for i in xrange(len(digits)-1, -1, -1):
            if not C: break
            
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                C = 1
            else:
                C = 0
        
        return digits if not C else [1] + digits
        
                