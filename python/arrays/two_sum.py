"""
Problem: Two Sum
Source: LeetCode
Link: https://leetcode.com/problems/two-sum/
Tags: Arrays, HashMap
"""


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
