# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self, A):
        tmp = A
        count = 0
        while tmp != None:
            count += 1
            tmp = tmp.next
        return count
            
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        len_A = self.length(A)
        len_B = self.length(B)
        tmp_A = A
        tmp_B = B
        
        diff = abs(len_A - len_B)
        if len_A > len_B:
            for _ in range(diff):
                tmp_A = tmp_A.next
        else:
            for _ in range(diff):
                tmp_B = tmp_B.next
        
        while tmp_A != tmp_B:
            tmp_A = tmp_A.next
            tmp_B = tmp_B.next
        
        return tmp_A
        
        
