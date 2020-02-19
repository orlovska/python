# Given an array nums and a value val, 
# remove all instances of that value in-place and return the new length.

class Solution(object):
    def removeElement(self, nums, val):
        for index in range(len(nums)):
            if index == len(nums):
                return len(nums)
                
            while nums[index] == val:
                nums.remove(nums[index])
                if index == len(nums):
                    return len(nums) 