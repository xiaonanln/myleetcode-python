HOURS = (1,2,4,8)
MINUTES = (1,2,4,8,16,32)

class Solution(object):
	def readBinaryWatch(self,num):
		"""
		:type num: int
		:rtype: List[str]
		"""
		sol = [-1] * num
		res = []

		def bt(i, beginPos, hour, minute):
			if hour >= 12 or minute >= 60: return

			if i == num:
				# print sol
				res.append( '%d:%02d' % (hour,minute) )
				return

			for pos in xrange(beginPos,10):
				sol[i] = pos
				bt(i+1,pos+1, hour+(HOURS[pos] if pos < 4 else 0), minute+(MINUTES[pos-4] if pos >= 4 else 0) )

		bt(0,0, 0, 0)
		return res


print Solution().readBinaryWatch(3)

# print list(sorted(['3:00','5:00','9:00','1:01','1:02','1:04','1:08','1:16','1:32','6:00','10:00','2:01','2:02','2:04','2:08','2:16','2:32','12:00','4:01','4:02','4:04','4:08','4:16','4:32','8:01','8:02','8:04','8:08','8:16','8:32','0:03','0:05','0:09','0:17','0:33','0:06','0:10','0:18','0:34','0:12','0:20','0:36','0:24','0:40','0:48']))
# print list(sorted(["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]))