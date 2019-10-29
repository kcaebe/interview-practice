"""
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
"""


from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            j = seen.get(num, None)
            if j != None:
                return [j, i]
            seen[target-num] = i
        return []


print(twoSum([1,2,6,4,5], 5))