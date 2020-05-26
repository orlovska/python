# Given a sorted array nums, 
# remove the duplicates in-place such that each element appear 
# only once and return the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        for index in range(1, len(nums)):
            if index == len(nums):
                return len(nums)
                
            while nums[index] == nums[index-1]:
                nums.remove(nums[index])
                if index == len(nums):
                    return len(nums)
               