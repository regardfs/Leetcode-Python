"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

URL: https://leetcode.com/problems/longest-palindromic-substring/?tab=Description

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand(s, n1, n2):
            l, r, n = n1, n2, len(s)
            while l >= 0 and r <= n - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        i, n = 0, len(s)
        longest_str = s[0]
        while i < n:
            l_s_1 = expand(s, i, i)
            if len(l_s_1) > len(longest_str):
                longest_str = l_s_1
            l_s_2 = expand(s, i, i + 1)
            if len(l_s_2) > len(longest_str):
                longest_str = l_s_2
            i += 1
        return longest_str