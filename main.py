# final version 

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    num_index = {} #make a dictionary to store both index and number
    for index, num in enumerate(nums): #use enumerate to keep track of the nums index
        complement = target - num #check the complement first
        if complement in num_index: #if complement already stored, return the complement and curent number index
            return [num_index[complement], index]
        
        num_index[num] = index #if not store just keep storing the num and index in the dictionary
    
    return [] #if no matching pairs found, return an empty list