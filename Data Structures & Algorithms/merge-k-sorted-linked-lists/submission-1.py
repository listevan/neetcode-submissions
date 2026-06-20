# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None
        cur = None

        while True:
            min_val = None
            min_ind = None

            for i, l in enumerate(lists):
                if not l:
                    # print("None")
                    continue
                # print(l.val)
                
                if min_val == None or l.val < min_val:
                    min_val = l.val
                    min_ind = i
            # print("*"*50)
            # print(min_val, min_ind)
            # print("*"*50)
                
            if min_val == None:
                break

            if not res:
                res = cur = lists[min_ind]
            else:
                cur.next = lists[min_ind]
                cur = cur.next
            
            lists[min_ind] = lists[min_ind].next

        return res
        