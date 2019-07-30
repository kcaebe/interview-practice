"""
Given an array nums of n integers where n > 1,  return an array output 
such that output[i] is equal to the product of all the elements of nums except nums[i].
"""

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        out = []
        prod = 1
        out.append(prod)
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            out.append(prod)
        
        prod = 1
        
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i+1]
            out[i] *= prod
        
        return out

print(productExceptSelf([1,2,3,4])) # -> [24,12,8,6]