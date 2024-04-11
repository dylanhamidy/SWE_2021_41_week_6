# initial version 

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    num_indices = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], index]
        
        num_indices[num] = index
    
    return []

# Example input
nums = [7, 11, 2, 15]
target = 9

# Call the function and print the result
result = twoSum(nums, target)
print("Output:", result)