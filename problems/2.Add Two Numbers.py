# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr_lsum = lsum = ListNode(0)
        addition = 0
        while True:
            ptr_lsum.val = l1.val + l2.val + addition
            if ptr_lsum.val >= 10:
                addition = 1
                ptr_lsum.val = ptr_lsum.val % 10
            else:
                addition = 0
            # check if the last addition    
            if l1.next == None and l2.next == None and addition == 0:
                break
            ptr_lsum.next = ListNode(0)
            ptr_lsum = ptr_lsum.next
            if l1.next != None:
                l1 = l1.next
            else:
                l1 = ListNode(0)
                
            if l2.next != None:
                l2 = l2.next
            else:
                l2 = ListNode(0)  
        return lsum

        
        