from heapq import *
class Solution(object):
	def isPossible(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if not nums: return False

		seqs0 = [] #seqs ends with the current num
		seqs1 = [] #seqs ends with the current num - 1

		pn = None
		for n in nums:
			if pn is not None:

				# print pn, n, seqs1, seqs0

				if n == pn:
					pass
				elif n == pn+1:
					for seqlen in seqs1:
						if seqlen < 3: return False
					seqs1, seqs0 = seqs0, []
				else:
					for seqlen in seqs0:
						if seqlen < 3: return False
					for seqlen in seqs1:
						if seqlen < 3: return False
					seqs0, seqs1 = [], []

			# print pn, n, seqs1, seqs0

			if seqs1:
				seqlen = heappop(seqs1)
				heappush(seqs0, seqlen+1)
			else: # we have to start a new seq
				heappush(seqs0, 1)

			# print pn, n, seqs1, seqs0

			pn = n

		# print seqs1, seqs0
		for seqlen in seqs0:
			if seqlen < 3: return False
		for seqlen in seqs1:
			if seqlen < 3: return False

		return True


# print Solution().isPossible([1,2,3,3,4,5])
print Solution().isPossible([1,2,3,3,4,4,5,5])
# print Solution().isPossible([1,2,3,4,4,5])