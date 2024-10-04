class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:      
        curr = ListNode(-1, next=head)
        result = curr

        for _ in range(n):
            head = head.next

        while head:
            curr = curr.next
            head = head.next  
        
        curr.next = curr.next.next

        return result.next
