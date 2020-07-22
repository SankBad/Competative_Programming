# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        curr = head
        count = 1
        while(count<m-1):
            curr = curr.next
            count += 1
        
        if curr.next==None:
            return head
        
        if m!=1:
            l = curr
            count += 1
            start = curr.next
            back = start
            curr = start.next
        else:
            start = curr
            back=start
            curr=start.next
        while(count<n):
            nextelem = curr.next
            curr.next = back
            back = curr
            curr = nextelem
            count += 1
            
        if m!=1:
            l.next = back
        else:
            head = back
        start.next = curr
        return head
