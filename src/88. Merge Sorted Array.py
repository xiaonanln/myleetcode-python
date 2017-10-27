class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2
        nums1.sort()
        # w = m+n-1
        # i, j = m-1, n-1
        # while i >= 0 and j >= 0:
        # 	if nums1[i] > nums2[j]:
        # 		nums1[w] = nums1[i]
        # 		i -= 1
        # 	else:
        # 		nums1[w] = nums2[j]
        # 		j -= 1
        # 	w -= 1
        #
        # while j >= 0:
        # 	nums1[w] = nums2[j]
        # 	w -= 1
        # 	j -= 1


nums1 = [1,2,3,0,0]
nums2 = [3,3]
Solution().merge(nums1, 3, nums2, 2)
print nums1
