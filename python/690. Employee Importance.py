"""
# Employee info
class Employee(object):
	def __init__(self, id, importance, subordinates):
		# It's the unique id of each node.
		# unique id of this employee
		self.id = id
		# the importance value of this employee
		self.importance = importance
		# the id of direct subordinates
		self.subordinates = subordinates
"""
from collections import deque
class Solution(object):
	def getImportance(self, employees, id):
		"""
		:type employees: Employee
		:type id: int
		:rtype: int
		"""
		e = employees[id-1]
		assert e.id == id
		q = deque([e])
		imp = 0
		while q:
			e = q.popleft()
			imp += e.importance
			for subid in self.subordinates:
				q.append(employees[subid-1])

		return imp









