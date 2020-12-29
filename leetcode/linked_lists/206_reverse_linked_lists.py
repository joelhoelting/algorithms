"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Iterative
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev = None
#         curr = head
#
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
#
#         return prev

# Recursive

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         # recursive: T O(n),  M O(n)
#
#         if not head:
#             return None
#
#         newHead = head
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None
#
#         return newHead
