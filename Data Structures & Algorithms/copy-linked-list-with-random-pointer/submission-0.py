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

        mapper = {}
        curr = head
        # map original nodes to copy nodes, init only the values
        # no pointers yet

        while curr:
            copy = Node(curr.val)
            mapper[curr] = copy
            curr = curr.next

        for node in mapper:
            orig = node
            copy = mapper[node]
            copy.next = mapper.get(orig.next)
            copy.random = mapper.get(orig.random)

        return mapper.get(head)








