class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        
        num3 = [value for value in nums1 if value in nums2]
        op = list(set(num3))
        return op