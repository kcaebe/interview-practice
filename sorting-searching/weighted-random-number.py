"""
Given an array w of positive integers, where w[i] describes the weight of index i, 
write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
"""



from typing import List
import bisect
import random
from collections import Counter

class RandomNumber:

    def __init__(self, w: List[int]):
        self.weights = w
        
        for i in range(1, len(w)):
            self.weights[i] += self.weights[i-1]
        
    def pickIndex(self) -> int:
        rnd = random.randint(1, self.weights[-1])
        return bisect.bisect_left(self.weights, rnd)


# Your Solution object will be instantiated and called as such:
w = [1, 2, 3, 4]
obj = RandomNumber(w)
param_1 = obj.pickIndex()

print(Counter([obj.pickIndex() for i in range(10000)]))
