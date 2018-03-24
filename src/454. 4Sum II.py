from bisect import bisect_left, bisect_right
class Solution(object):
	def fourSumCount(self, A, B, C, D):
		"""
		:type A: List[int]
		:type B: List[int]
		:type C: List[int]
		:type D: List[int]
		:rtype: int
		"""
		if not A or not B or not C or not D: return 0
		X = [n1+n2 for n1 in A for n2 in B]
		Y = [n1+n2 for n1 in C for n2 in D]
		X.sort()
		Y.sort()
		i = 0
		j = len(Y)-1
		count = 0
		LX = len(X)
		while i < LX and j >= 0:
			s = X[i] + Y[j]
			if s < 0:
				i += 1
			elif s > 0:
				j -= 1
			else:
				# s == 0
				x = X[i]
				c1 = 0
				while i < LX and X[i] == x:
					i += 1
					c1 += 1

				y = Y[j]
				c2 = 0
				while j >= 0 and Y[j] == y:
					j -= 1
					c2 += 1
				count += c1 * c2
		return count


A=[-1,-1]
B=[-1,1]
C=[-1,1]
D=[1,-1]
print Solution().fourSumCount(A,B,C,D)
