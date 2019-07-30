"""
Given an input string , reverse the string word by word. 

Do this in place

"""

from typing import List

def reverseWords(s: List[str]):
    reverse(s, 0, len(s) - 1)
    start = 0
    for i, v in enumerate(s):
        if v == " ":
            reverse(s, start, i - 1)
            start = i + 1
            
    reverse(s, start, len(s) - 1)
        
def reverse(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1    
arr = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
reverseWords(arr)
print(arr)
# -> ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]