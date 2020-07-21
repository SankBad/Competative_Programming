# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        back = None
        curr = head
        while(curr):
            nextelem = curr.next
            curr.next = back
            back = curr
            curr = nextelem
        
        head = back
        return head
