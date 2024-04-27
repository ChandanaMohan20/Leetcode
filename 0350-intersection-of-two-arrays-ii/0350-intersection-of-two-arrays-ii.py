class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num3=[]
       
        for value in nums1:
            if value in nums2:
                num3.append(value)
                nums2.remove(value)
                
        return num3
        
        