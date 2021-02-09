## Input: array, target
## Output: array
# Function: find the indices of the values of the array that add to target. 
# Assumptions: You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(nums, target):
    num_dict = {}
    for i,val in enumerate(nums):
        num_dict[target-val]=i
        if val in num_dict:
            return i,num_dict[val]


nums = [2,7,11,15] 
target = 9
print(twoSum(nums,target))
