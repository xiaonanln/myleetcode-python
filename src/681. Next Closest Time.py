class Solution(object):
	def nextClosestTime(self, t):
		"""
		:type time: str
		:rtype: str
		"""

		chars = list(set(t[0] + t[1] + t[3] + t[4]))
		t = map(int, t.split(':'))
		# print chars, t

		sol = []
		minsol = [999, 999]

		def distance(tt):
			if tt > t:
				hour = tt[0] - t[0]
				min = tt[1] - t[1]
				# print 'distance1', tt, t, hour * 60 + min
				return hour * 60 + min
			else:
				dto24 = (24 - t[0]) * 60 + (0 - t[1])
				# print 'distance2', tt, t, tt[0] * 60 + tt[1] + dto24
				return tt[0] * 60 + tt[1] + dto24

		def smaller(t1, t2):
			# print 'compare', t1, t2
			return distance(t1) < distance(t2)

		def bt():
			if len(sol) == 4:
				newt = [int(sol[0]+sol[1]), int(sol[2] + sol[3])]
				# print 'sol', newt
				if smaller(newt, minsol):
					minsol[:] = newt
					# print 'minsol', minsol
				return

			i = len(sol)
			for c in chars:
				if i == 0 and c > '2': continue
				elif i == 1 and sol[0] == '2' and c > '4': continue
				elif i == 2 and c >= '6': continue

				sol.append( c )
				bt()
				sol.pop()

		bt()
		return '%02d:%02d' % (minsol[0], minsol[1])

print Solution().nextClosestTime("19:34")
print Solution().nextClosestTime("23:59")
print Solution().nextClosestTime("22:22")