"""
Given a non-empty array of integers, every element appears twice except for one. 

Find that single one.

"""

from typing import List
def singleNumber(nums: List[int]) -> int:
        tot = 0
        for num in nums:
            tot ^= num 
        return tot


print(singleNumber([4,1,2,1,2])) # -> 4