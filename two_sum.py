# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


def twoSum(nums, target):
    for i in range(len(nums)):
        searched_number = target - nums[i]
        for j in range(i):
            if nums[j] == searched_number:
                return [i,j]
                
# test
print(twoSum([2,3,7,9], 9))
print(twoSum([3,2,4], 6))

                


