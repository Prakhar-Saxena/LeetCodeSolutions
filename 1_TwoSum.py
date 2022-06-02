class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in d and d[comp] != i:
                return [i,d[comp]]