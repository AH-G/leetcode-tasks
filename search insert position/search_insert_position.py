class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return(0)
        elif target>nums[len(nums)-1]:
            return(len(nums))
        elif target<nums[0]:
            return(0)
        for i in range(len(nums)):
            if nums[i]==target:
                return(i)
            elif target>nums[i]:
                if i<len(nums)-1:
                    if target<nums[i+1]:
                        return(i+1)
