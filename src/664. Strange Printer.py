class Solution(object): # still wrong
	def strangePrinter(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		L = len(s)
		dp = [[0] * (L+1) for _ in xrange(L+1)]
		for i in xrange(L):
			dp[i][i+1] = 1

		possibleChars = [set([s[i]])  for i in xrange(L)]
		for l in xrange(2, L+1): # l = 1 ~ L
			for i in xrange(0, L-l+1):
				j = i + l # check substring [i, j)
				subs = s[i:j]
				pc = possibleChars[i]
				pc.add(s[j-1])

				minPC = l
				for basechar in pc:
					sp = subs.split(basechar)
					idx = 0
					printCount = 1
					for _subs in sp:
						if _subs != '':
							# print 'subs', _subs, idx, idx+len(_subs), dp[idx][idx+len(_subs)]
							printCount += dp[i+idx][i+idx+len(_subs)]

						idx += len(_subs) + 1
					# print sp, printCount
					minPC = min(minPC, printCount)

				dp[i][j] = minPC
				# print l, i, j, pc,minPC

		# for r in dp:
		# 	print r

		return dp[0][L]

print Solution().strangePrinter("dddccbdbababaddcbcaabdbdddcccddbbaabddb")