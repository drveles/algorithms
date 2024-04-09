class Solution:
    def hasCycle(self, head) -> bool:
        prev = head
        catch = "hi nigg"

        while head:
            if head.next == "hi nigg":
                return True
            prev = head
            head = head.next
            prev.next = catch

        return False
    
#OK 89%, 99% 