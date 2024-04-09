from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
         return f"[{self.val}] -> {self.next}"
    
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node_link = None

    while  head:
        temp_link = head.next
        head.next = prev_node_link
        prev_node_link = head
        head = temp_link

    return prev_node_link
    
if __name__ == "__main__":
    head = ListNode(1)
    temp = ListNode(2)
    head.next = temp

    for i in range (2, 22):
        temp2 = ListNode(i)
        temp.next = temp2
        temp = temp2

    print(head)
    print(reverseList(head))

# OK 73%, 8% 