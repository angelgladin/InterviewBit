# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution:
    def length(self, A):
        r = 0
        current = A
        while current is not None:
            current = current.next
            r+=1
        return r
     
    def move_pointers(self, A):
        current = A
        prev = None
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
    
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        l = self.length(A)
        n = l//2
        current = A
        i = 0
        while i < n:
            current = current.next
            i+=1
        head = A
        tail = self.move_pointers(current)
        tail_aux = tail
        i = 0
        while i < n:
            head.val = tail.val - head.val
            head = head.next
            tail = tail.next
            i+=1
        tail_aux = self.move_pointers(tail_aux)
        return A
        