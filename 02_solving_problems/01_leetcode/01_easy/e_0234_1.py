# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev_slow = None
        temp_slow = slow
        while temp_slow:
            temp_link = temp_slow.next
            temp_slow.next = prev_slow
            prev_slow = temp_slow
            temp_slow = temp_link
        
        while prev_slow:
            if prev_slow.val != head.val:
                return False
            prev_slow = prev_slow.next
            head = head.next

        return True

#OK, 86%, 61%
