# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        previous = None
        counter = 0
        while curr != None:
            counter += 1
            curr = curr.next
            
        
        curr = head
        if n == counter:
            return head.next
        for i in range (counter):
            if (counter - i) == n:
                curr = curr.next
                previous.next = curr
                break 
            else:
                previous = curr
                curr = curr.next
                
        curr = head
        return curr