#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s.isspace():
            return 1
        s_lst = list(s)
        lst = []
        max_len = 0
        for i in range(len(s_lst)):
            c = s_lst[i]
            if c not in lst:
                lst.append(c)
            else:
                len_lst = len(lst)
                if len_lst > max_len:
                    max_len = len_lst
                res = [x for x in range(len(lst)) if lst[x] == c]
                lst = lst[res[0]+1:]
                lst.append(c)
            len_lst = len(lst)
            if len_lst > max_len:
                max_len = len_lst
        return max_len