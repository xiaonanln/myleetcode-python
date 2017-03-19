class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if not S: return []
        if not L: return []
        
        wordcount = len(L)
        wordlen = len(L[0])
        wordappear = {}
        
        for word in L:
            wordappear[word] = wordappear.get(word, 0) + 1
#         print wordappear
        
        DL = (wordappear.keys())
#         print DL
        
        wordindex = {}
        for i, word in enumerate(DL):
            wordindex[word] = i
            
        wordappear = [wordappear[word] for word in DL]
        
#         print wordindex, wordappear

        result = []
        for start in xrange(wordlen):
            words = []
            for i in xrange(start, len(S)-wordlen + 1, wordlen):
                word = S[i:i+wordlen]
                wi = wordindex.get(word, -1)
                words.append(wi)
            
#             print words
            rec = [0] * len(DL)
            wstart = 0
            
            for i, wi in enumerate(words):
#                 print rec, wi, wordappear
                
                if wi == -1:
                    wstart = i + 1
                    rec = [0] * len(DL)
                    continue 
                
                if i - wstart + 1 > wordcount:
                    rec[ words[wstart] ] -= 1
                    wstart += 1
                
                rec[wi] += 1
                if rec[wi] > wordappear[wi]:
                    while words[wstart] != wi:
                        rec[words[wstart]] -= 1
                        wstart += 1
                        
                    rec[words[wstart]] -= 1
                    wstart += 1 #skip the word
                    
                if i - wstart + 1 == wordcount:
                    result.append(start + wstart * wordlen)
            
        return result

# S = "barfoothefoobarman"
# L = ["foo", "bar"]
# print Solution().findSubstring(S, L)

S, L = "a", ["a"]
S, L = "babaabba", ["ba","ab"]
print Solution().findSubstring(S, L)

