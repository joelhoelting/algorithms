"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
(1) -> (2) -> (4)
(1) -> (3) -> (4)
Output: (1)->(1)->(2)->(3)->(4)->(4)

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def mergeTwoLists(l1, l2):
#     head = ListNode()
#     curr = head

#     while l1 and l2:
#         if l1 and l2 and l1.val <= l2.val:
#             curr.next = l1
#             l1 = l1.next
#         elif l1 and l2 and l1.val >= l2.val:
#             curr.next = l2
#             l2 = l2.next
#         curr = curr.next
#     curr.next = l1 or l2

#     return head.next


def mergeTwoLists(l1, l2):
    dummy = node = ListNode(0)

    while l1 and l2:
        if l1.val <= l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next

        node = node.next

    node.next = l1 if l1 else l2

    return dummy.next


mergeTwoLists('node1', 'node2')
