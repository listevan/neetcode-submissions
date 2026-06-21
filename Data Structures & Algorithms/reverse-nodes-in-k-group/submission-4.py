# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c = head
        h = head
        p = None
        next_p = None
        n = None

        res = None

        while True:
            # print(f"beginning")
            c = h
            for i in range(k):
                if not c:
                    # print("Returning")
                    return res
                # print(f"first check: c: {c.val}, h: {h.val}")
                c = c.next

            n = c

            c = h
            hc = None
            for i in range(k):
                # print(f"reversal: c: {c.val}, h: {h.val}")
                nc = c.next
                c.next = hc
                hc = c
                c = nc

            if p:
                p.next = hc
            else:
                res = hc
            p = h
            h.next = n

            # pp = res
            # while pp:
            #     print(f"pp: {pp.val}")
            #     pp = pp.next

            h = n