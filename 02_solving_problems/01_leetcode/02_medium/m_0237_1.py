# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # это интересно, node является ссылкой вида prev.next, 
        # но как будто перезаписать node = node.next не получится, так как запишу в локальную переменную
        # upd, и правда не работает.
        # а если стянуть следующие ноды на место текущей. врядли смотрят на указатели, важны значения.

        # while node.next.next: 
        #     node.val = node.next.val
        #     node = node.next
        # node.val = node.next.val
        # node.next = None

        # более того, мне не нужно стягивать все значения, достаточно следующей ноды и пропустить её!

        node.val = node.next.val
        node.next = node.next.next
