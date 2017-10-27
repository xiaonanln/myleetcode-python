class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        self.mapping = {
                "1": "", 
                "2": "abc",
                "3": "def",
                "4": "ghi", 
                "5": "jkl", 
                "6": "mno", 
                "7": "pqrs", 
                "8": "tuv", 
                "9": "wxyz", 
                "0": "",
                "*": "",
                "#": "",  
                }
        return self.solve(digits, 0)
    
    def solve(self, digits, start):
        if start == len(digits):
            return [ '' ]
        
        d = digits[start]
        subresults = self.solve(digits, start+1)
        if self.mapping[d] == '':
            return subresults
        
        return [c + result for result in subresults for c in self.mapping[d]] 
        
print Solution().letterCombinations("2")
    