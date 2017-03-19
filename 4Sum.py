# file encoding: utf8
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# 
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
# 
#     A solution set is:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)

# Solution4 Accepted!
import sys

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        buffer = {}
        return self._solve(num, 0, 4, target, buffer)
    
    def _solve(self, num, start, n, target, buffer):
        key = (start, n, target)
        if key in buffer:
            return buffer[key]
        
        result = self._real_solve(num, start, n, target, buffer)
        buffer[key] = result
        return result
    
    def _real_solve(self, num, start, n, target, buffer):
        if n == 0 and target == 0:
            return [ [] ]
        
        if n == 0: return []
        
        if start >= len(num): return []
        if len(num) - start < n: return []
        
        if len(num) - start == n:
            s = sum(num[start:])
            if s == target:
                return [num[start:]]
            else:
                return []

        s1 = self._solve(num, start+1, n, target, buffer)
        s2 = self._solve(num, start+1, n-1, target - num[start], buffer)
        s2 = [[num[start]] + s for s in s2]
        
        return s1 + s2
    

class Solution2:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        
        num_max_sums = []
        for i in xrange(len(num)):
            maxes = []
            for n in xrange(1, 5):
                minsum = sum(num[i:i+n])
                maxsum = sum(num[len(num) - n:])
                maxes.append( (minsum, maxsum) )
            num_max_sums.append(maxes)
        
        queue = [ ([], 0) ]
        result = []
        
        for i, n in enumerate(num):
            maxsums = num_max_sums[i]
            toappend = []
            
            for sol, s in queue:
                leftn = 4 - len(sol)
                minsum, maxsum = maxsums[leftn - 1]
                
                if s + minsum > target: continue 
                if s + maxsum < target: continue
                
                #print sol, s, new_sol, new_s
                if len(sol) < 3:
                    new_sol = sol + [n]
                    new_s = s + n
                    toappend.append( ( new_sol, new_s ) )
                else: 
                    new_s = s + n
                    if new_s == target:
                        new_sol = sol + [n]
                        result.append(new_sol)
        
            queue += toappend
        
        for r in result:
            print r, sum(r)
        return result


class Solution3:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
    
        R1 = []
        for i, n in enumerate(num):
            R1.append( ((n, ), n, (i, )) )
        
        R2 = []
        for i in xrange(len(R1)):
            for j in xrange(i+1, len(R1)):
                assert R1[i][2] != R1[j][2]
                R2.append( (R1[i][0] + R1[j][0], R1[i][1] + R1[j][1], 
                            R1[i][2] + R1[j][2]))
        print len(R2)

        result = []                
        for i, ri in enumerate(R2):
            maxi = ri[2][1] 
            jstart = (len(num)-1 + len(num)-1 - maxi) * (maxi + 1) / 2
            if jstart >= len(R2): continue 
            
            for j, rj in enumerate(R2[jstart:]):
                if ri[1] + rj[1] != target: continue
                if [x for x in ri[2] if x in rj[2]]:
                    continue 
                
                sol = ri[0] + rj[0]
                result.append(list(sol))
        
        return result
                
                    
class Solution4:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
    
        R1 = []
        for i, n in enumerate(num):
            R1.append( ((n, ), n, (i, )) )
        
        R2 = []
        for i in xrange(len(R1)):
            for j in xrange(i+1, len(R1)):
                assert R1[i][2] != R1[j][2]
                R2.append( (R1[i][0] + R1[j][0], R1[i][1] + R1[j][1], 
                            R1[i][2] + R1[j][2]))
        
        H2 = {}
        for r in R2:
            if r[1] not in H2: H2[r[1]] = []
            H2[r[1]].append(r)
        
        
        distinct_results = set()
        result = []
        for i, ri in enumerate(R2):
            left = target - ri[1]
            if left not in H2: continue 
            for rj in H2[left]:
#                 print >>sys.stderr, ri, rj
                if ri[2][1] >= rj[2][0]: continue 
                
                sol = ri[0] + rj[0]
                if sol not in distinct_results:
                    distinct_results.add(sol)
                    result.append(list(sol))
                
        return result
                    
sol = Solution4()
print sol.fourSum([-2, -1, 0, 0, 1, 2], 0)
print sol.fourSum([-500,-481,-480,-469,-437,-423,-408,-403,-397,-381,-379,-377,-353,-347,-337,-327,-313,-307,-299,-278,-265,-258,-235,-227,-225,-193,-192,-177,-176,-173,-170,-164,-162,-157,-147,-118,-115,-83,-64,-46,-36,-35,-11,0,0,33,40,51,54,74,93,101,104,105,112,112,116,129,133,146,152,157,158,166,177,183,186,220,263,273,320,328,332,356,357,363,372,397,399,420,422,429,433,451,464,484,485,498,499], 2139)
print sol.fourSum([91277418,66271374,38763793,4092006,11415077,60468277,1122637,72398035,-62267800,22082642,60359529,-16540633,92671879,-64462734,-55855043,-40899846,88007957,-57387813,-49552230,-96789394,18318594,-3246760,-44346548,-21370279,42493875,25185969,83216261,-70078020,-53687927,-76072023,-65863359,-61708176,-29175835,85675811,-80575807,-92211746,44755622,-23368379,23619674,-749263,-40707953,-68966953,72694581,-52328726,-78618474,40958224,-2921736,-55902268,-74278762,63342010,29076029,58781716,56045007,-67966567,-79405127,-45778231,-47167435,1586413,-58822903,-51277270,87348634,-86955956,-47418266,74884315,-36952674,-29067969,-98812826,-44893101,-22516153,-34522513,34091871,-79583480,47562301,6154068,87601405,-48859327,-2183204,17736781,31189878,-23814871,-35880166,39204002,93248899,-42067196,-49473145,-75235452,-61923200,64824322,-88505198,20903451,-80926102,56089387,-58094433,37743524,-71480010,-14975982,19473982,47085913,-90793462,-33520678,70775566,-76347995,-16091435,94700640,17183454,85735982,90399615,-86251609,-68167910,-95327478,90586275,-99524469,16999817,27815883,-88279865,53092631,75125438,44270568,-23129316,-846252,-59608044,90938699,80923976,3534451,6218186,41256179,-9165388,-11897463,92423776,-38991231,-6082654,92275443,74040861,77457712,-80549965,-42515693,69918944,-95198414,15677446,-52451179,-50111167,-23732840,39520751,-90474508,-27860023,65164540,26582346,-20183515,99018741,-2826130,-28461563,-24759460,-83828963,-1739800,71207113,26434787,52931083,-33111208,38314304,-29429107,-5567826,-5149750,9582750,85289753,75490866,-93202942,-85974081,7365682,-42953023,21825824,68329208,-87994788,3460985,18744871,-49724457,-12982362,-47800372,39958829,-95981751,-71017359,-18397211,27941418,-34699076,74174334,96928957,44328607,49293516,-39034828,5945763,-47046163,10986423,63478877,30677010,-21202664,-86235407,3164123,8956697,-9003909,-18929014,-73824245], -236727523)
