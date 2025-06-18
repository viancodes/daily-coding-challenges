# LeetCode Problem: Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each node contains a single digit.
# Add the two numbers and return the sum as a new linked list.

# Sample Input:
# l1 = [2, 4, 3], l2 = [5, 6, 4]
# Explanation: 342 + 465 = 807
# Sample Output:
# [7, 0, 8]  # because digits are stored in reverse order

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10

            current.next = ListNode(new_digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
