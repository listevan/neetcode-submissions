# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        for i in range(n):
            front = front.next
        
        back = head
        prev = None
        while front:
            prev = back
            back = back.next
            front = front.next
        
        if not prev:
            return head.next
        
        prev.next = back.next
        return head