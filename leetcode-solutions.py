#--------------------------------------------------------------------------------------------------------------
# 1. TWO SUMS
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#-------------------------------------------------------------------------------------------------------------
from typing import List

class Solution:
    def __init__(self):
        return

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1 in range(len(nums)):
            target_pair = target - nums[idx1]
            for idx2 in range(idx1+1,len(nums)):
                if nums[idx2] == target_pair:
                    return([idx1,idx2])
                
# Test TWO SUMS
nums = [2,7,11,15]
target = 9
solution = Solution()
print("TWO SUMS: Test - Expected output [0, 1]")
print(solution.twoSum(nums,9))
