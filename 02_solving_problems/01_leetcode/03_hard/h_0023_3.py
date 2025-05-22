# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        templist = list()
        result = head = ListNode()
        for idx in range(len(lists)):
            while lists[idx]:
                templist.append(lists[idx].val)
                lists[idx] = lists[idx].next
        
        templist.sort()

        for val in templist:
            node = ListNode(val)
            head.next = node
            head = head.next

        return result.next