#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            d[numbers[i]] = i
        for i in range(len(numbers)):
            comp = target-numbers[i]
            if comp in d and d[comp] != i:
                return [i+1,d[comp]+1]

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            d[numbers[i]] = i
        for i in range(len(numbers)):
            comp = target-numbers[i]
            if comp in d and d[comp] != i:
                return [i+1,d[comp]+1]