# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_val = 0
        tail = ListNode()
        head = tail 

        while l1 or l2:
            temp_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + temp_val 

            tail.next = ListNode(val=(temp_sum % 10))
            temp_val = temp_sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            tail = tail.next

        if temp_val: 
            tail.next = ListNode(val=temp_val)
            
        return head.next
    
#OK, 80%, 10%