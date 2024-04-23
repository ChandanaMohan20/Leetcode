class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numlen = len(nums)
        inc = 1
        dec = 1
        maxlen = 0
        if numlen==1:
            maxlen = 1
            return maxlen

        else:
            for i in range (1,numlen):
                if (nums[i-1]< nums[i]):
                    inc = inc + 1
                    dec = 1
                    maxlen = max(inc,dec, maxlen)
                
                elif (nums[i-1]> nums[i]):
                    inc = 1
                    dec = dec + 1
                    maxlen = max(inc,dec, maxlen)
                    
                else:
                    inc = 1
                    dec = 1
                    maxlen = max(inc,dec, maxlen)
            return maxlen