
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
        M = len(vals) // 2
        return vals[0:M] == vals[:-M-1:-1]

import utils
print Solution().isPalindrome(utils.makelist(1,2,3,2,1))