#https://leetcode.com/problems/reverse-integer/
def is32bit(x: int) -> bool:
    if (x < (-2147483648)) or (x > 2147483647):
        return False
    else:
        return True


class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        if (x == 0) or not is32bit(x):  # x < ((-1) * (2 ** 31) ) or x > ((2 ** 31) - 1):
            return output
        elif x < 0:
            output = int(str(x * (-1))[::-1]) * (-1)
        else:
            output = int(str(x)[::-1])

        if not is32bit(output):
            return 0
        else:
            return output