# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node_link = None

        while  head:
            temp_link = head.next
            head.next = prev_node_link
            prev_node_link = head
            head = temp_link

        return prev_node_link   

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
        slow = self.reverseList(slow)

        while head.next and slow.next:
            head_c = head.next
            head.next = slow
            slow = slow.next
            head = head.next
            head.next = head_c
            head = head.next

#OK 74%, 86%