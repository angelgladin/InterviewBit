# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        # There's at least 1 node
        if A is None:
            return None
        fast = A.next
        slow = A
        loop = False
        while not False and fast is not None and fast.next is not None and slow is not None:
            if fast is slow:
                loop = True
                break
            fast = fast.next.next
            slow = slow.next
        if loop:
            s = set()
            loop_len = 1
            fast = fast.next
            while slow != fast:
                fast = fast.next
                s.add(id(fast))
                loop_len += 1
            
            head = A
            while True:
                if id(head) in s:
                    return head
                else:
                    head = head.next
        else:
            return None
        return fast
