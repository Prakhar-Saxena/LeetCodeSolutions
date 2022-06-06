#https://leetcode.com/problems/median-of-two-sorted-arrays/
def findMedian(nums: List[int]):
    len_nums = len(nums)
    if len_nums % 2 == 0:
        len_nums_div_by_2 = int(len_nums / 2)
        return (nums[len_nums_div_by_2 - 1] + nums[len_nums_div_by_2]) / 2
    else:
        return nums[int((len_nums / 2) - 0.5)]


def isEmpty(lst: List[int]):
    if len(lst) == 0:
        return True
    else:
        return False


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        list1 = nums1
        list2 = nums2

        while list1 or list2:
            if (not list2 or (list1 and list1[0] < list2[0])):
                merged.append(list1[0])
                list1 = list1[1:]
            elif (not list1 or (list2 and list1[0] >= list2[0])):
                merged.append(list2[0])
                list2 = list2[1:]
        print(merged)
        return findMedian(merged)