# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution(object):
	def rotateRight(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		if not head: return None 
		p = head 
		listLen = 0 # calculate list length 
		while p:
			p = p.next
			listLen += 1

		k = k % listLen # now k < listLen
		if k == 0: 
			return head 

		p1 = head; p2 = head 
		for _ in xrange(k): 
			p2 = p2.next 

		assert p2 

		while p2.next:
			p1 = p1.next 
			p2 = p2.next 

		newHead = p1.next 
		p1.next = None 
		p2.next = head 

		return newHead
		
from utils import *

printlist(Solution().rotateRight(makelist(1,2 ,3 ,4 ,5), 2))