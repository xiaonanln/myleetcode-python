


class SolutionDP : 
    def combinationSum2(self, candidates, target):
        candidates.sort()
        useCount = {}
        for c in candidates:
            useCount[c] = useCount.get(c, 0) + 1
        candidates = sorted(useCount.keys())
#         print candidates, useCount
        
        if not candidates: return []
        if candidates[0] > target: return []
        
        N = len(candidates)
        DP = [None] * (N+1) # DP[i] ==> numbers can be added from candidates[0:i], so DP[N] is what we want
        DP[0] = [ (0, () ) ]
        result = []
        
        for i in xrange(1, N+1):
            n = candidates[i-1]
            uc = useCount[n]
            dp = list(DP[i-1])
            
            for _sum, nums in DP[i-1]:
                assert _sum < target
                for _uc in xrange(uc):
                    _sum, nums = _sum + n, nums + (n, )
                    if _sum < target:
                        dp.append( (_sum, nums) )
                    elif _sum == target:
                        result.append( (nums) )
                        break
                    else:
                        break 
            
            DP[i] = dp
        
        return map(list, set(result))

print SolutionDP().combinationSum2([10,1,2,7,6,1,5], 8)
print SolutionDP().combinationSum2([13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19], 25)