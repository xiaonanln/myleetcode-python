class SolutionBad(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nums = sorted(str(_) for _ in xrange(1, n+1))
        return int(nums[k-1])

class SolutionBetter(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        v = 1
        k -= 1

        while k > 0:
            # generate the next number
            if v * 10 <= n:
                v *= 10
            else:
                v = v + 1
                if v > n and v % 10 != 0: # if v > n, make v % 10 == 0
                    v += 10 - (v % 10)

                while v % 10 == 0:
                    v = v // 10

            k -= 1

        return v

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        v = 1
        k -= 1

        while k > 0:
            # generate the next number

            v2 = v + 1
            if v2 <= n:
                nd = 0
                while v2 * 10 <= n: 
                    v2 *= 10
                    nd += 1
                tn = sum(10 ** _ for _ in xrange(0, nd+1))
                print v, v2, nd, tn
                if k > tn:
                    k -= tn
                    v += 1
                    continue 

            if v * 10 <= n:
                v *= 10
            else:
                v = v + 1
                if v > n and v % 10 != 0: # if v > n, make v % 10 == 0
                    v += 10 - (v % 10)

                while v % 10 == 0:
                    v = v // 10

            k -= 1

        return v



# print SolutionBad().findKthNumber(4289384, 1922239)
# print SolutionBad().findKthNumber(10, 3)
# print SolutionBetter().findKthNumber(10, 3)
# print Solution().findKthNumber(10, 3)

# print Solution().findKthNumber(4289384, 1922239)
# print Solution().findKthNumber(7747794, 5857460)
# print Solution().findKthNumber(9885387, 8786251)

# print SolutionBetter().findKthNumber(9885387, 8786251)

print Solution().findKthNumber(10, 3)
# print Solution().findKthNumber(13, 2)
# print SolutionBetter().findKthNumber(5202363, 3078011)
# print Solution().findKthNumber(5202363, 3078011)