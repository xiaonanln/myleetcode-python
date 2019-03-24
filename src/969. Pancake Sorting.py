class Solution(object):
	def pancakeSort(self, A):
		end = len(A) - 1
		ret = []
		while end > 0:
			# find the max
			maxindex = None
			maxval = None
			for i in xrange(0, end+1):
				if maxindex is None or maxval < A[i]:
					maxindex = i
					maxval = A[i]

			if maxindex != end:
				if maxindex != 0:
					ret.append(maxindex+1)
					A[:maxindex+1] = A[:maxindex+1][::-1]

				ret.append(end+1)
				A[:end+1] = A[:end+1][::-1]

			end = end - 1

		return ret



