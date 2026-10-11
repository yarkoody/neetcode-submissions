# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        #find middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #put a pointer on the first node after the middle and split the lists
        second = slow.next
        slow.next = None

        #reverse from slow onward
        prev = None
        while second:
            sec_next = second.next
            second.next = prev
            prev = second
            second = sec_next
        second = prev
        #merge
        while first and second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second
        

