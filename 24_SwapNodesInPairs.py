#https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        swap = True
        head_ = head
        current = head
        if not head or not head.next:
            return head
        while current.next:
            if swap:
                current_val = current.val
                current.val = current.next.val
                current.next.val = current_val
            swap = not swap
            current = current.next
        return head_