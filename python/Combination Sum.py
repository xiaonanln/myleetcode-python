import collections

class SolutionDFS: # Accepted, 852 ms
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        
        q = collections.deque()
        N = len(candidates)
        for i in xrange(N):
            q.append( (i, ) )
            
        result = []
        while q:
            inds = q.popleft()
            s = sum(candidates[i] for i in inds)
            if s == target:
                result.append( list(inds) )
            
            elif s > target:
                pass
            else: # if s < target
                lastind = inds[-1]
                for ind in xrange(lastind, N):
                    q.append( inds + (ind, ) )
        
        return [ [candidates[ind] for ind in sol] for sol in result]

class SolutionDP : 
    def combinationSum(self, candidates, target):
        candidates.sort()
        if not candidates: return []
        if candidates[0] > target: return []
        if  candidates[0] == target:
            return ([ [ candidates[0] ] ])
        
            
        N = len(candidates)
        DP = [None] * (N+1) # DP[i] ==> numbers can be added from candidates[0:i], so DP[N] is what we want
        DP[0] = [ (0, () ) ]
        result = []
        
        for i in xrange(1, N+1):
            n = candidates[i-1]
            dp = list(DP[i-1])
            
            for _sum, nums in DP[i-1]:
                
                assert _sum < target
                _sum, nums = _sum + n, nums + (n, )
                while _sum < target:
                    dp.append( (_sum, nums) )
                    _sum, nums = _sum + n, nums + (n, )
                
                if _sum == target:
                    result.append( list(nums) )
            
            DP[i] = dp
        
        return result

print SolutionDP().combinationSum([1], 1)