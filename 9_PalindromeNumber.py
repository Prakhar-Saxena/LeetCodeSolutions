#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rev = 0
        while num > 0:
            dig = num % 10
            rev = rev * 10
            rev = rev + dig
            num = int(num/10)
        if x == rev:
            return True
        else:
            return False