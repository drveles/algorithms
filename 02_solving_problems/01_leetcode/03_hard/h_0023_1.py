# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for head in lists:
            while head:
                heap.append(head.val)
                head = head.next
        if not heap: return
        head_res = res = ListNode()
        heapq.heapify(heap)
        while(len(heap)):
            temp = ListNode(heapq.heappop(heap))
            res.next = temp
            res = res.next
    
        return head_res.next

#OK 95%, 34%