# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        stack = []

        while head:
            stack.append(ListNode(head.val))
            head = head.next

        temp = result = stack.pop()
        while stack:
            temp.next = stack.pop()
            temp = temp.next

        return result
