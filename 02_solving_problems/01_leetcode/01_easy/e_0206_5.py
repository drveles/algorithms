class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        while head:
            temp_next = head.next
            head.next = prev
            prev = head
            head = temp_next
        
        return prev
