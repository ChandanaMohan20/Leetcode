class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        a = {}
        for i in nums1:
            for j in nums2:
                sumval = i+j
                if sumval in a:
                    a[sumval]+=1
                else:
                    a[sumval] = 1
        sumval = 0
        count = 0
              
        for i in nums3:
            for j in nums4:
                sumval = -(i+j)
                if sumval in a:
                    count+=a[sumval]
        return count
                