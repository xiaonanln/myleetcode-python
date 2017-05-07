"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        print len(s)
        def ispalindrome(i, j):
            sub = s[i:j]
            return sub == sub[::-1]
            
        N = len(s)
        dp = [[None]*(N+1) for _ in xrange(N+1)]
        for L in xrange(0, N+1):
            for i in xrange(0, N-L+1):
                j = i + L
                # print N, L, i, j
                if ispalindrome(i, j):
                    dp[i][j] = 0
                    continue 

                mc = float('inf')
                for k in xrange(i+1, j):
                    mc = min(mc, dp[i][k] + dp[k][j] + 1)
                
                dp[i][j] = mc
                
        return dp[0][N]

print Solution().minCut('aab')
import cProfile
cProfile.run("Solution().minCut('apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp')")