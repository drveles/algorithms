# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = str(l1.val)
        s2 = str(l2.val)
        head = ptr = ListNode()

        while l1.next:
            l1 = l1.next
            s1 = str(l1.val) + s1

        while l2.next:
            l2 = l2.next
            s2 = str(l2.val) + s2
        
        for c in str(int(s1) + int(s2))[::-1]:
            temp_node = ListNode(int(c))
            ptr.next = temp_node
            ptr = ptr.next

        return head.next