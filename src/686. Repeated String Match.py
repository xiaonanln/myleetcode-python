class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if B in A:
            return 1

        LA, LB = len(A), len(B)
        n = (LB + LA - 1) // LA
        if B in A * n:
            return n
        elif B in A * (n + 1):
            return n + 1
        else:
            return -1