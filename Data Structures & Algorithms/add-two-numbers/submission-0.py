# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0

        c1, c2 = l1, l2
        p2 = None
        while c1 and c2:
            c2.val += c1.val + carry
            carry = 0
            if c2.val >= 10:
                carry = 1
                c2.val -= 10

            p2 = c2
            c1, c2 = c1.next, c2.next

        if c1:
            p2.next = c1
            c2 = c1
        
        while carry:
            if not c2:
                c2 = ListNode(0)
                p2.next = c2
            c2.val += 1
            carry = 0
            if c2.val >= 10:
                carry = 1
                c2.val -= 10
            p2 = c2
            c2 = c2.next
        
        return l2
