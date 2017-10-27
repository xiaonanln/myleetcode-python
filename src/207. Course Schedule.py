
from collections import deque
class Solution(object):
	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		numPrerequisites = [0] * numCourses
		requiring = [[] for _ in xrange(numCourses)]

		for req in prerequisites:
			a, b = req # a requires b
			numPrerequisites[a] += 1
			requiring[b].append( a )


		finishCourseCount = 0
		Q = deque()
		for course, numReq in enumerate(numPrerequisites):
			if numReq == 0:
				Q.append(course) # push learnable course to Q

		while Q:
			course = Q.pop()
			# learn it
			finishCourseCount += 1

			for otherCourse in requiring[course]:
				numPrerequisites[otherCourse] -= 1
				if numPrerequisites[otherCourse] == 0:
					Q.append(otherCourse)

		return finishCourseCount == numCourses

print Solution().canFinish( 0, [] )	
print Solution().canFinish( 1, [[0,0]] )
print Solution().canFinish( 2, [[1,0]] )
print Solution().canFinish( 2, [[1,0],[0,1]] )