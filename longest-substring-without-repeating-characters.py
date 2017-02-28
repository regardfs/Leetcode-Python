"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
subsequence and not a substring.
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/?tab=Description
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start_index, visited = 0, 0, [False for _ in xrange(256)]
        for index, val in enumerate(s):
            if visited[ord(val)]:
                while val != s[start_index]:
                    visited[ord(s[start_index])] = False
                    start_index += 1
                start_index += 1
            else:
                visited[ord(val)] = True
            longest = max(longest, index-start_index+1)
        return longest