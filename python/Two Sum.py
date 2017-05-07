class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num = list(enumerate(num))
        num.sort(cmp=Solution.compare)
        
        h = 0
        t = len(num) - 1
        
        while h < t:
            s = num[h][1] + num[t][1]
            if s < target:
                h += 1
            elif s > target:
                t -= 1
            else:
                h, t = num[h][0]+1, num[t][0]+1
                return (h, t) if h < t else (t, h)
                
                
    @staticmethod
    def compare(n1, n2):
        return cmp(n1[1], n2[1])