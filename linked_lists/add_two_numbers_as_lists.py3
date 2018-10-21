# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        head = None
        res_pointer = None
        
        a_current = A
        b_current =  B
        ac = 0
        while a_current is not None or b_current is not None:
            r = ac
            if a_current is not None:
                r += a_current.val
                a_current = a_current.next
            if b_current is not None:
                r += b_current.val
                b_current = b_current.next
            
            if r>9:
                ac = 1
            else:
                ac = 0
            
            new = ListNode(r%10)
            if head is None:
                head = new
                res_pointer = head
            else:
                res_pointer.next = new
                res_pointer = new
        
        if ac == 1:
            res_pointer.next = ListNode(1)
        return head
        
        