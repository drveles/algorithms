# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_head = ListNode(val=None, next=head)
        left = temp_head 
        right = head
        count_iter = 0

        while right.next: 
            if count_iter >= n - 1:
                left = left.next
            right = right.next
            count_iter += 1
        
        left.next = left.next.next if left.next.next else None

        return temp_head.next

#OK, 29%, 7%
