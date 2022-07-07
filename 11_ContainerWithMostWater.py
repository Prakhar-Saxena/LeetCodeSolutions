#https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        left = 0
        right = n - 1
        while left < right:
            hl, hr = height[left], height[right]
            current = min(hl, hr) * (right - left)
            max_area = max(current, max_area)
            if (hl < hr):
                left += 1
            else:
                right -= 1
        return max_area
