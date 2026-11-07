# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        my_array = []
        second_array = []

        while curr:
            my_array.append(curr)
            curr = curr.next

        for i in range (len(my_array) - 1, -1, -1):
            second_array.append(my_array[i])

        if not second_array:
            return None
            
        for i in range (len(second_array) -1):
            second_array[i].next = second_array[i + 1]
        second_array[-1].next = None
        return second_array[0]