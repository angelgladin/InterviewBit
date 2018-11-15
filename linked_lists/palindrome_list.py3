# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def len_aux(self, A):
        r = 0
        current = A
        while current is not None:
            current = current.next
            r+=1
        return r
    
    def reverse_pointers(self, A):
        previous = None
        current = A
        next_node = None
        
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
    
        return previous
    
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        n = self.len_aux(A)
        half = (n//2) if n%2==0 else (n//2)+1
        current = A
        half_node = A

        for _ in range(half):
            half_node = half_node.next
        
        tail = self.reverse_pointers(half_node)
        
        for _ in range(n//2):
            if current.val != tail.val:
                return 0
            current = current.next
            tail = tail.next
        
        return 1
