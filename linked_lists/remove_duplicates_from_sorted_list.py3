# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        current_node = A
        next_node = None
        while current_node is not None:
            next_node = current_node.next
            while next_node is not None and current_node.val == next_node.val:
                next_node = next_node.next
            current_node.next = next_node
            current_node = current_node.next
        return A
