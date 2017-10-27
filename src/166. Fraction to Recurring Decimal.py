import time 

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0: return '0'
        if numerator < 0 and denominator < 0:
            return self.fractionToDecimal(-numerator, -denominator)
        elif numerator < 0 or denominator < 0:
            return '-' + self.fractionToDecimal(abs(numerator), abs(denominator))

        a, b = divmod(numerator, denominator)
        if b == 0:
            return str(a)

        return str(a)+'.' + self.getDecimal(b, denominator)

    def getDecimal(self, num, denominator):
        res = ''
        dot = False 

        visitedNums = {}
        while num != 0:
            if num in visitedNums:
                # print 'repeat!', num, res[visitedNums[num]:]
                repeatStart = visitedNums[num]
                return res[:repeatStart] + '(' + res[repeatStart:] + ')'

            visitedNums[num] = len(res)

            num *= 10
            if num < denominator:
                res += '0'
            else:
                # print res, num, denominator
                a, b = divmod(num, denominator)
                res += str(a)
                num = b

        return res 




        

print Solution().fractionToDecimal(2, 1)
print Solution().fractionToDecimal(1, 2)
print Solution().fractionToDecimal(2, 3)
print Solution().fractionToDecimal(4, 9)
print Solution().fractionToDecimal(4, 333)