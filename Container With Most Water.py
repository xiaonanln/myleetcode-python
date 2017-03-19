class Solution:
    # @return an integer
    def maxArea(self, height):
#         print height
        R = []
        Ra = 0
        R.append(len(height))
        for i in xrange(len(height)-1, -1, -1):
            h = height[i]
            if h <= Ra:
                continue 
            else:
                for j in xrange(Ra+1, h+1):
                    R.append(i)
                Ra = h
                assert len(R) == h + 1
        
        L = [-1]
        La = 0            
        for i in xrange(len(height)):
            h = height[i]
            if h <= La: continue 
            for j in xrange(La+1, h+1):
                L.append(i)
            La = h
            assert len(L) == h+1
        
#         print L, R
        
        hmax = -1
        smax = -1
        for i, h in enumerate(height):
            if h <= hmax: continue
            hmax = h
            r = R[hmax]
            s = (r - i) * hmax
#             print i, h, r, s
            if smax < s:
                smax = s
        
#         print L, R
        hmax = -1
        for i in xrange(len(height)-1, -1, -1):
            h = height[i]
            if h <= hmax: continue
            hmax = h
            l = L[hmax]
            s = (i - l) * hmax
            if smax < s:
                smax = s
        
        return smax
    
# print Solution().maxArea([1, 2, 3, 4, 5])
print Solution().maxArea([1,2])