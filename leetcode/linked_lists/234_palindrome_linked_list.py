"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        return arr == arr[::-1]


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        fast = head
        slow = self.reverse(slow)

        while slow:
            if slow.val != fast.val:
                return False

            slow = slow.next
            fast = fast.next

        return True

    def reverse(self, head):
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
