# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]
        # i, j = 0, len(vals) - 1
        # while i < j:
        #     if vals[i] != vals[j]: return False
        #     i += 1; j -= 1
        #
        # return True



import utils
print Solution().isPalindrome(utils.makelist(1,2,3,2,1))