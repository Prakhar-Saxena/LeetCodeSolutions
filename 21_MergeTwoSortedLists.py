#https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1 and not list2):
            return None
        elif (not list1):
            return list2
        elif (not list2):
            return list1

        head = ListNode()
        current = head

        while (list1 or list2):
            if (not list2 or (list1 and list1.val < list2.val)):
                current.val = list1.val
                list1 = list1.next
            elif (not list1 or (list2 and list1.val >= list2.val)):
                current.val = list2.val
                list2 = list2.next
            if (list1 or list2):
                current.next = ListNode()
                current = current.next
        return head