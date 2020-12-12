"""Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

begin to intersect at node c1.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:

Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_list_a = 0
        len_list_b = 0

        a_pointer = headA
        while a_pointer:
            len_list_a += 1
            a_pointer = a_pointer.next

        b_pointer = headB
        while b_pointer:
            len_list_b += 1
            b_pointer = b_pointer.next

        loop_difference = 0

        if len_list_a > len_list_b:
            loop_difference = len_list_a - len_list_b
            while loop_difference:
                loop_difference -= 1
                headA = headA.next

        if len_list_a < len_list_b:
            loop_difference = len_list_b - len_list_a
            while loop_difference:
                headB = headB.next
                loop_difference -= 1

        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next


# Using a stack
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stackA, stackB = [], []

        while headA:
            stackA.append(headA)
            headA = headA.next

        while headB:
            stackB.append(headB)
            headB = headB.next

        solution = None

        while stackB and stackA:

            a, b = stackA.pop(), stackB.pop()
            if a != b:
                solution = a.next
                break
            else:
                solution = a

        return solution


# Using a set
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    list1 = set()
    root1 = headA
    root2 = headB
    while root1:
        list1.add(root1)
        root1 = headA.next
        headA = root1
    while root2:
        if root2 in list1:
            return root2
        else:
            root2 = headB.next
            headB = root2
    return root2
