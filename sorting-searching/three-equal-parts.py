"""
Given an array A of 0s and 1s, divide the array into 3 non-empty parts such that 
all of these parts represent the same binary value.

If it is possible, return any [i, j] with i+1 < j, such that:

A[0], A[1], ..., A[i] is the first part;
A[i+1], A[i+2], ..., A[j-1] is the second part, and
A[j], A[j+1], ..., A[A.length - 1] is the third part.
All three parts have equal binary value.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents.  
For example, [1,1,0] represents 6 in decimal, not 3.  Also, leading zeros are allowed, 
so [0,1,1] and [1,1] represent the same value.
"""


from typing import List

def threeEqualParts(arr: List[int]) -> List[int]:
        ones = arr.count(1)
        bin_str = "".join(map(lambda v: str(v), arr))
        if ones % 3 != 0:
            return [-1, -1]
        elif ones == 0:
            return [0, len(arr)-1]
        ones //= 3
        sig_zeros = 0
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                sig_zeros += 1
            else:
                break

        cur_ones, cur_zeros = 0, 0
        left_val, mid_val, right_val = 0, 0, 0
        indicies = []
        for ind, bit in enumerate(arr):
            if bit == 1:
                cur_ones += 1
            elif bit == 0 and cur_ones >= ones:
                cur_zeros += 1

            if cur_ones > ones or cur_zeros > sig_zeros:
                return [-1, -1]

            if cur_ones == ones and cur_zeros == sig_zeros:
                if len(indicies) == 0:
                    indicies.append(ind)
                    left_val = int(bin_str[:ind+1], 2)
                else:
                    indicies.append(ind + 1)
                    i = indicies[0]
                    j = indicies[1]
                    if left_val == int(bin_str[i+1:j], 2) == int(bin_str[j:], 2):
                        return indicies
                    else:
                        return [-1, -1]
                cur_ones, cur_zeros = 0, 0
        return [-1,-1]

print(threeEqualParts([0,1,0,1,0,1])) # -> 1,4
print(threeEqualParts([0,1,1,0,0,1,1,0,0,0,1,1,0])) # -> 3,8