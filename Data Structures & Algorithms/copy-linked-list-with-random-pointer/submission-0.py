"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr:
            new_node = Node(curr.val, curr.next, None)
            curr.next = new_node
            curr = new_node.next
        
        curr = head
        while curr:
            new_node = curr.next
            new_node.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        curr = head
        new_head = curr.next if curr else None
        while curr:
            new_node = curr.next
            curr.next = new_node.next
            curr = curr.next
            new_node.next = curr.next if curr else None


        return new_head