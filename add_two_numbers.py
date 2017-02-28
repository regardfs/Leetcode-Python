"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
URL: https://leetcode.com/problems/add-two-numbers/?tab=Description
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = []
        p1 = l1
        p2 = l2
        left_val = 0
        while p1 is not None or p2 is not None:
            if p1 is not None and p2 is not None:
                if (p1.val + p2.val + left_val) >= 10:
                    val, left_val = (p1.val + p2.val + left_val) % 10, int((p1.val + p2.val + left_val) / 10)
                else:
                    val, left_val = (p1.val + p2.val + left_val) % 10, 0
            if p2 is None and p1 is not None:
                if (p1.val + left_val) >= 10:
                    val, left_val = (p1.val + left_val) % 10, int((p1.val + left_val) / 10)
                else:
                    val, left_val = (p1.val + left_val) % 10, 0
            if p2 is not None and p1 is None:
                if (p2.val + left_val) >= 10:
                    val, left_val = (p2.val + left_val) % 10, int((p2.val + left_val) / 10)
                else:
                    val, left_val = (p2.val + left_val) % 10, 0
            l.append(val)
            p1 = p1.next if hasattr(p1, "next") else None
            p2 = p2.next if hasattr(p2, "next") else None
        if left_val:
            l.append(left_val)
        return l