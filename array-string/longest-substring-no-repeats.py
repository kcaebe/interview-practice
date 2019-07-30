
"""
Given a string, find the length of the longest substring 
without repeating characters.
"""

def lengthOfLongestSubstring(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    seen = set(s[0])
    l, r, cnt = 0, 1, 1
    while r < len(s):
        if s[l] == s[r]:
            l += 1
            r += 1
        elif s[r] not in seen:
            seen.add(s[r])
            r += 1
        else:
            seen.remove(s[l])
            l += 1
        cnt = max(cnt, len(seen))
    return cnt


print(lengthOfLongestSubstring("abcabcbb")) # -> 3
print(lengthOfLongestSubstring("bbbbb")) # -> 1
print(lengthOfLongestSubstring("pwwkew")) # -> 3