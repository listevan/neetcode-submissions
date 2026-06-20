# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_h = None
        curr = None
        if not list1:
            return list2
        if not list2:
            return list1

        while list1 and list2:
            if list1.val < list2.val:
                if not curr:
                    new_h = curr = list1
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next
            else:
                if not curr:
                    new_h = curr = list2
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next
        
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return new_h