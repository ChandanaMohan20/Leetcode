class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        k = len(nums1)
        for i in range(0,n):
            nums1[k-i-1] = nums2[i]
            
        nums1.sort()