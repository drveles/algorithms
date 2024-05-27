# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        tail = result = ListNode()
        temp_min = 0

        while True:
            temp_min = None

            for idx in range(len(lists)):
                if lists[idx]:
                    if temp_min is None: 
                        temp_min = idx
                    if lists[idx].val < lists[temp_min].val:
                        temp_min = idx
            
            if temp_min is None:
                break
            tail.next = lists[temp_min]
            tail = tail.next
            lists[temp_min] = lists[temp_min].next

        
        return result.next
    
# OK 5%, 73%