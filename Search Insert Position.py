class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return(nums.index(target))
        else:
          for i in range(len(nums)):
            if target<nums[i]:
                return(i)
                break
            elif target>nums[len(nums)-1]:
                return(len(nums))
                break
 
