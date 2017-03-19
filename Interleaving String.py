class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1)+len(s2): return False 
        L1, L2 = len(s1), len(s2)
        dp = [None] * (L2+1)
        dp[0] = True

        for i in xrange(0, L1+1):
            for j in xrange(0, L2+1):
            	if i == j == 0: continue 
            	
            	m1 = i > 0 and s1[i-1] == s3[i+j-1]
            	m2 = j > 0 and s2[j-1] == s3[i+j-1]
            	if m1 and m2:
            		dp[j] = dp[j] or dp[j-1]
            	elif m1:
            		dp[j] = dp[j]
            	elif m2:
            		dp[j] = dp[j-1]
            	else:
            		dp[j] = False

        return dp[L2]

print Solution().isInterleave("", "", "")
print Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
print Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")