# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

class Solution(object):
    def searchInsert(self, nums, target):
        
        for index in range(len(nums)):
            if nums[index] >= target:
                return index 
        return len(nums)