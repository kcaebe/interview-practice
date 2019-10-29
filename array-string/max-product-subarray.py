

def maxProd(nums):
    max_here = min_here = nums[0]
    tot_max = tot_min = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        print(max_here, min_here ,num)
        max_here = max(num, max_here * num, min_here * num)
        min_here = min(num, max_here * num, min_here * num)
        tot_max = max(tot_max, max_here)
        tot_min = min(tot_min, min_here)
    return tot_max


print(maxProd([2, 3, -2, 4]))
