# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    # NOT PROUD, I COULD DO IT BETTER
    def reverseBetween(self, A, B, C):
        if B == C:
            return A
        
        current = A
        a = None
        b = None
        a_sub = None
        b_sub = None
        i = 1
        while current is not None:
            if i == B-1:
                a = current
            elif i == B:
                a_sub = current
            elif i == C+1:
                b = current
            elif i == C:
                b_sub = current
            i += 1
            current = current.next
        
        b_sub.next = None
        if a is not None:
            a.next = None
        
        current = a_sub
        prev = None
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        if a is not None:
            a.next = b_sub
            
        
        a_sub.next = b


        return A