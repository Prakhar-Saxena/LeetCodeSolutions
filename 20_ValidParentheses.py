#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        openers = ['(', '{', '[']
        closers = [')', '}', ']']
        opener_closer = {'(': ')',
                        '{': '}',
                        '[': ']'}
        s_list = list(s)
        s_inv = []
        for x in s:
            if (x in openers):
                s_inv.append(x)
            else: # x in closers
                if ((len(s_inv) == 0) or (opener_closer[s_inv[-1]] != x)):
                    return False
                if (opener_closer[s_inv[-1]] == x):
                    s_inv.pop()
        if (len(s_inv) == 0):
            return True
        else:
            return False