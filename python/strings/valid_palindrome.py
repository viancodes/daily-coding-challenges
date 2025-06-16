"""
Problem: Valid Palindrome
Source: LeetCode
Link: https://leetcode.com/problems/valid-palindrome/
Tags: Strings, Two Pointers
"""

def is_palindrome(s):
    filtered = [char.lower() for char in s if char.isalnum()]
    return filtered == filtered[::-1]

# Test
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
