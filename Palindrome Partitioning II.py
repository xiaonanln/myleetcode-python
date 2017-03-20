class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        ispalindrome = [[False] * (N+1) for _ in xrange(N+1)]

        for L in xrange(0, N+1):
            for i in xrange(0, N-L+1):
                j = i + L
                if L <= 1:
                    ispalindrome[i][j] = True
                else:
                    ispalindrome[i][j] = ispalindrome[i+1][j-1] and s[i] == s[j-1]

                # print L, i, j, ispalindrome[i][j]

        dp = [[None]*(N+1) for _ in xrange(N+1)]
        for L in xrange(0, N+1):
            for i in xrange(0, N-L+1):
                j = i + L
                # print N, L, i, j, ispalindrome[i][j]
                if ispalindrome[i][j]:
                    dp[i][j] = 0
                    continue 

                mc = float('inf')
                for k in xrange(i+1, j):
                    mc = min(mc, dp[i][k] + dp[k][j] + 1)
                
                dp[i][j] = mc
                
        return dp[0][N]


class Solution2(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}

        def ispalindrome(i, j):
            # print i, j
            if j <= i + 1:
                return True

            try:
                return cache[(i, j)]
            except KeyError:
                j = j - 1
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1
                cache[(i, j)] = res = i >= j
                return res

        N = len(s)
        dp = [[None] * (N + 1) for _ in xrange(N + 1)]
        for L in xrange(0, N + 1):
            for i in xrange(0, N - L + 1):
                j = i + L
                # print N, L, i, j
                if ispalindrome(i, j):
                    dp[i][j] = 0
                    continue

                mc = float('inf')
                for k in xrange(i + 1, j):
                    mc = min(mc, dp[i][k] + dp[k][j] + 1)

                dp[i][j] = mc

        return dp[0][N]


print Solution().minCut("aab")
print Solution().minCut("ababababababababababababcbabababababababababababa")
print Solution().minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")