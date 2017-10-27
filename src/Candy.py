
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if len(ratings) <= 1: return len(ratings)
        
        done = False
        give = [1] * len(ratings)
        for i in xrange(len(ratings)):
            doleft = i == 0 or ratings[i] <= ratings[i-1]
            doright = i == len(ratings) - 1 or ratings[i] <= ratings[i+1]
            if doleft and doright:
                j = i
                while j > 0 and ratings[j - 1] > ratings[j]:
                    give[j-1] = max(give[j-1], give[j] + 1)
                    j -= 1
                
                j = i
                while j < len(ratings) - 1 and ratings[j+1] > ratings[j]:
                    give[j+1] = max(give[j+1], give[j] + 1)
                    j += 1
                    
        for i in xrange(len(ratings)):
            if i > 0 and ratings[i] > ratings[i-1] and give[i] <= give[i-1]:
                give[i] = give[i-1]+1
            
            if i < len(ratings)-1 and ratings[i] > ratings[i+1] and give[i] <= give[i+1]:
                give[i] = give[i+1]+1
                
        return sum(give)
    
    
print Solution().candy([5,1,1,1,10,2,1,1,1,3])