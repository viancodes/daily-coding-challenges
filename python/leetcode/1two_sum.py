"""
06/18/2025
LeetCode Problem: Two Sum
Given an array of integers `nums` and a target integer `target`,
return the indices of the two numbers such that they add up to `target`.
You may not use the same element twice, and only one solution will always exist.

Sample Input:
nums = [2, 7, 11, 15], target = 9
Sample Output:
[0, 1]  # Because nums[0] + nums[1] = 2 + 7 = 9"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        This method finds and returns the indices of two numbers in the list `nums`
        that add up to the specified `target`. Each input list has exactly one valid solution,
        and the same element cannot be used twice.
        """

        # Step 1: Initialize an empty dictionary to store numbers we've seen so far.
        # The dictionary maps a number to its index in the array.
        num_map = {}

        # Step 2: Iterate over the list with both index and number using enumerate.
        for index, num in enumerate(nums):

            # Step 3: Calculate the "complement" — the number needed to reach the target.
            complement = target - num

            # Step 4: Check if that complement is already in the map (i.e., seen before).
            # If yes, return the index of the complement and the current number.
            if complement in num_map:
                return [num_map[complement], index]

            # Step 5: If not found, store this number and its index in the dictionary
            # so we can refer to it later.
            num_map[num] = index

        # Step 6: Just in case (though problem states one solution always exists)
        return []
