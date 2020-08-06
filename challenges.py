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

# class Solution: # FAIL - works but too time complex
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         index1 = 0
#         solution = []
#         list_length = len(nums)
#         while index1 < list_length:
#             index2 = index1+1
#             while index2 < list_length:
#                 if nums[index1] + nums[index2] == target:
#                     solution.append(index1)
#                     solution.append(index2)
#                     return solution
#                 index2+=1
#             index1+=1  
            

#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         solution = []
#         x = nums[0]
#         for y in nums:
#             if x + y = target:
#                 solution.append(x)
#                 solution.append(index2)
#                 return solution

#             index2 = x+1
#             while index2 < list_length:
#                 if nums[x] + nums[index2] == target:
#                     solution.append(x)
#                     solution.append(index2)
#                     return solution
#                 index2+=1
#             x+=1    

#---------------------------------------------
# Factorial - example of recursion
#---------------------------------------------
def factorial(n):
    
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#---------------------------------------------
# Countdown - two ways - recursion and not
#---------------------------------------------

def count_down(start):
    #If we've reached 0 already, print 0 but do not call
    #another copy
    if start <= 0:
        print(start)
    
    #If we haven't reached 0 yet, print the current number,
    #then call count_down with the current number minus 1.
    else:
        print(start)
        count_down(start - 1)

def count_down2(start): # without recursion
    print(start)
    for i in reversed(range(start)):
        print(i)

def count_down3(start): # without recursion or python functions
    while start >= 0:
        print(start)
        start -= 1


#---------------------------------------------
# Fibonacci - build a dictionary as you go
#---------------------------------------------
solved_already={} # store fibs that we solve along the way
def fib(n):
    # should check that n is positive integer here...
    if n in solved_already:
        return solved_already[n] # avoid re-calculating in recursion
    
    if n == 1 or n == 2:
        result = 1
    else:
        result =  fib(n - 1) + fib(n - 2)
    solved_already[n]=result
    return result

# Test
for n in range(1,101):
    print("fib(", n ,") =", fib(n))