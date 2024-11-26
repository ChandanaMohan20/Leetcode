class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        for i in range(0,n):
            l = i+1
            r = n-1
            
            while(l<r):
                numsum = nums[i]+nums[l]+nums[r]
                if numsum>= target:
                    r = r-1
                else:
                    res = res+ r-l
                    l = l+1
        
        return res