"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
URL: https://leetcode.com/problems/two-sum/
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            if target - i in nums:
                if nums.count(i) > 1:
                    f_index = nums.index(i)
                    nums.remove(i)
                    return [f_index, nums.index(target-i)+1]
                elif nums.index(i) != nums.index(target-i):
                    return [ nums.index(i), nums.index(target-i)]