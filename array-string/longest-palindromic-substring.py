"""
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.
"""

def longestPalindrome(s: str) -> str:
    pal = ""
    for i in range(len(s)):
        possible = find_palindrome(s, i, i)
        pal = possible if len(possible) > len(pal) else pal
        possible = find_palindrome(s, i, i+1)
        pal = possible if len(possible) > len(pal) else pal
    return pal


def find_palindrome(s, l, r):
    while (l >= 0) and (r <= len(s) - 1) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


print(longestPalindrome("cbbd"))# -> bb
print(longestPalindrome("babad"))# -> bab or aba