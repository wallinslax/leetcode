# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        preNode = None
        while head:
            nextNode = head.next
            head.next = preNode
            # move to next
            preNode = head
            head = nextNode

        return preNode
            

            
        