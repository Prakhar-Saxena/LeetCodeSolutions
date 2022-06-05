#https://leetcode.com/problems/longest-common-prefix/
def yada(strs: List[str], prefix: str) -> bool:
    for s in strs:
        if not s.startswith(prefix):
            return False
    return True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key=len)
        while prefix != '':
            if (yada(strs, prefix)):
                return prefix
            prefix = prefix[:-1]
        return prefix