class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        overall_max=0
        if nums:
            max_up_to_here=nums[0]
            overall_max=nums[0]
        else:
            return(None)
        for i in range(1,len(nums)):
            max_up_to_here=max(nums[i],max_up_to_here+nums[i])
            if overall_max<max_up_to_here:
                overall_max=max_up_to_here
        return(overall_max)
