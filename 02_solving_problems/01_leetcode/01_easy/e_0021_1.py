def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
    head = ListNode()
    temp = head

    while list1 and list2:
        if list1.val < list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    
    temp.next = list1 or list2

    return head.next

#OK 80%, 58%