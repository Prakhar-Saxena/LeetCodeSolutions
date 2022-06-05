#https://leetcode.com/problems/implement-strstr/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)
        if needle == haystack:
            return 0
        for i in range(0, len_haystack - len_needle + 1):
            print('haystack[i:i+len_needle]: ' + haystack[i:i+len_needle])
            if (haystack[i:i+len_needle] == needle):
                return i
        return -1