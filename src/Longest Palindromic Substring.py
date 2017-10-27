class Solution: # TLE
    # @return a string
    def longestPalindrome(self, s):
        self.indices = {}
        for i, c in enumerate(s):
            if c not in self.indices: self.indices[c] = []
            self.indices[c].append(i)
        
        print self.indices
        longestStart, longestStop = 0, -1
        for c, inds in self.indices.iteritems():
            for i in xrange(len(inds)):
                ind1 = inds[i]
                print 'ind1', ind1
                for j in xrange(len(inds)-1, i-1, -1):
                    ind2 = inds[j]
                    print 'ind2', ind2
                    if ind2 - ind1 + 1 <= longestStop - longestStart + 1: continue 
                    
                    if self.isPalindrome(s, ind1, ind2):
                        longestStart = ind1
                        longestStop = ind2
                        print 'longest', longestStart, longestStop
                        break 
        
        return s[longestStart:longestStop+1]
    
    def isPalindrome(self, s, ind1, ind2):
        while ind1 < ind2:
            if s[ind1] != s[ind2]: return False
            ind1 += 1
            ind2 -= 1
        return True

class Solution: # TLE, but java version AC. Java version listed bellow
    # @return a string
    def longestPalindrome(self, s):
        if len(s) <= 1: return s
        N = len(s)
        M = []
        for i in xrange(N):
            m = [False] * N
            M.append(m)
        
        M[N-1][N-1] = True
        
        longest = (0, 0)
        for i in xrange(N-1):
            M[i][i] = True
            M[i][i+1] = s[i] == s[i+1]
            if M[i][i+1]:
                longest = (i, i+1)
        
#         print M
        
        for step in xrange(2, N):
            longestFoundInStep = False
            for i in xrange(0, N - step):
                stop = i + step
                mv = (s[i] == s[stop]) and M[i+1][stop-1]
                M[i][stop] = mv
                if not longestFoundInStep and mv:
#                     print "got longest", stop - i + 1
                    longest = (i, stop)
                    longestFoundInStep = True
        
        return s[longest[0]: longest[1]+1]
          
## JAVA VERSION DP which got AC
# public class Solution {
#     public String longestPalindrome(String s) {
#         if (s.length() <= 1) return s; 
#         
#         int N = s.length(); 
#         boolean[][]M = new boolean[N][N]; 
#         int start = 0, end = 0; 
#         for (int i = 0; i < N-1; i++) {
#             M[i][i] = true; 
#             M[i][i+1] = s.charAt(i) == s.charAt(i+1);
#             if (M[i][i+1]) {
#                 start = i; end = i + 1; 
#             }
#         }
#         M[N-1][N-1] = true; 
#         
#         for (int step = 2; step < N; step++) {
#             for (int i = 0; i < N - step; i++) {
#                 int stop = i + step;
#                 boolean mv = M[i+1][stop-1] && s.charAt(i) == s.charAt(stop); 
#                 M[i][stop] = mv; 
#                 if (mv) {
#                     start = i; end = stop; 
#                 }
#             }
#         }
#         
#         return s.substring(start, end+1); 
#     }
# }

print Solution().longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")
# print Solution().longestPalindrome('bb')
# print Solution().longestPalindrome('a')    
# print Solution().longestPalindrome('abcddcbaxxx')
# print Solution().longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


