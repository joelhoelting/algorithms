# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None

        currNode = ListNode()
        currNode.next = head
        head = currNode

        while currNode.next:
            if currNode.next.val == val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next

        return head.next

    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     if not head:
    #         return head
    #
    #     curr = head
    #
    #     while curr and curr.next:
    #         if curr.next.val == val:
    #             curr.next = curr.next.next
    #         else:
    #             curr = curr.next
    #     return head.next if head.val == val else head
