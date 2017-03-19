class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        if not s: return False
        s = s.strip()
        if not s: return False
        
        return self.solve(s, False)
    
    def solve(self, s, pureinteger):
        if not s: return False
        
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        
        dot = 0
        exp = 0
        gotanydigit = False
        gotanydigitaftere = False
        for i, d in enumerate(s):
            if d == '.':
                if pureinteger: return False
                
                if dot == 0: 
                    if not exp: dot = 1
                    else: return False
                else: return False
            
            elif d in '0123456789': 
                gotanydigit = True
                if exp != 0:
                    gotanydigitaftere = True
                    
            elif d == 'e':
                if pureinteger: return False
                
                if exp == 0:
                    if gotanydigit: 
                        return self.solve(s[i+1:], True)
                        
                    else: return False
                else: return False
        
            else:
                return False
            
        return gotanydigit and (( exp and gotanydigitaftere ) or (not exp))
            
             
        
    
assert(Solution().isNumber("0") == True)
assert(Solution().isNumber(" 0.1") == True)
assert(Solution().isNumber("abc") == False)
assert(Solution().isNumber("1 a") == False)
assert(Solution().isNumber("2e10") == True)
assert(Solution().isNumber("2e") == False)
assert(Solution().isNumber(    " 005047e+6") == True)
assert(Solution().isNumber(    "92e1740e91") == False)




