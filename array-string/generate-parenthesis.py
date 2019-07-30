"""
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.
"""

from typing import List

def all_parens(n, m, s, parens):
    if n == 0 and m == 0:
        parens.append(s)
        return parens
    if n > 0:
        all_parens(n-1, m, s + "(", parens)
    if m > n:
        all_parens(n, m-1, s + ")", parens)
    return parens

def generateParenthesis(n: int) -> List[str]:
    return all_parens(n, n, "", [])


print(generateParenthesis(3))
# [ "((()))", "(()())", "(())()", "()(())", "()()()" ]