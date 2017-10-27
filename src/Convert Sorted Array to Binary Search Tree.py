# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.solve(num, 0, len(num))
    
    def solve(self, nums, start, stop):
        if stop <= start:
            return None
        
        mid = (start + stop) // 2
        head = TreeNode( nums[mid] )
        head.left = self.solve(nums, start, mid)
        head.right = self.solve(nums, mid+1, stop)
        return head
    
print Solution().sortedArrayToBST([3,5,8])