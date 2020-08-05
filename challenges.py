#---------------------------------------------
# 1. TWO SUMS
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#---------------------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1 = 0
        solution = []
        list_length = len(nums)
        while index1 < list_length:
            index2 = index1+1
            while index2 < list_length:
                if nums[index1] + nums[index2] == target:
                    solution.append(index1)
                    solution.append(index2)
                    return solution
                index2+=1
            index1+=1   
