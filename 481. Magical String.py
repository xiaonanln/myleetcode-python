class Solution(object):
	def magicalString(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n == 0: return 0
		elif n <= 3: return 1	
		
		seq = [1, 2, 2]
		i = 2
		num1 = 1
		lastnum = 2
		while len(seq) < n:
			if seq[i] == 1:
				lastnum = 3 - lastnum
				seq.append( lastnum )
				i += 1
			else: # seq.i == 2
				lastnum = 3 - lastnum
				seq.append(lastnum)
				seq.append(lastnum)
				i += 1

		assert len(seq) in (n, n+1)
		if len(seq) == n+1:
			seq[-1:] = []

		return seq.count(1)



print Solution().magicalString(6)

print Solution().magicalString(100)

print Solution().magicalString(100000)