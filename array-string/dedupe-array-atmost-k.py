
"""
Given a sorted array nums, remove the duplicates in-place such that 
duplicates appeared at most k times and return the new length.

Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.
"""

from typing import List
def removeDuplicates(nums: List[int], k = 2) -> int:
    if len(nums) <= 2:
        return len(nums)
    l = 0
    allowDupes = k-1
    for r in range(1, len(nums)):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
            allowDupes = k-1
        elif allowDupes > 0:
            l += 1
            nums[l] = nums[r]
            allowDupes -= 1
        
    return l + 1

inp = [1,1,1,2,2,3]
end = removeDuplicates(inp)
print(inp[:end])
# -> [1,1,2,2,3]

inp = [0,0,1,1,1,1,2,3,3]
end = removeDuplicates(inp)
print(inp[:end])
# -> [0,0,1,1,2,3,3]