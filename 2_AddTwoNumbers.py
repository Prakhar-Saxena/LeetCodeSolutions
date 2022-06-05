#https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getSumAndCarry(n1: int, n2: int):  # assume n1 and n2 are single digit numbers
    summation = n1 + n2
    return (summation % 10), (summation // 10)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1 and not l2):
            return None
        elif (not l1):
            return l2
        elif (not l2):
            return l1

        head = ListNode()
        current = head
        carry = 0

        while l1 or l2:
            if not l1:
                summation = 0 + l2.val
                current.val, carry = getSumAndCarry(summation, carry)
                l2 = l2.next
            elif not l2:
                summation = l1.val + 0
                current.val, carry = getSumAndCarry(summation, carry)
                l1 = l1.next
            else:
                summation = l1.val + l2.val
                current.val, carry = getSumAndCarry(summation, carry)
                l1 = l1.next
                l2 = l2.next
            if (l1 or l2):
                current.next = ListNode()
                current = current.next
            elif carry != 0:
                current.next = ListNode()
                current = current.next
                current.val = carry
        return head