# Two Sum LeetCode Solution
# https://leetcode.com/problems/two-sum/description/
# twubz 2024-06-06
"""
Given an array of integers nums and an integer target, 
return the indices i and j such that 
nums[i] + nums[j] == target 
and i != j.

You may assume that every input has exactly one pair 
of indices i and j that satisfy the condition.

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in num_to_index:
                return [num_to_index[compliment],i]
            num_to_index[num] = i

       

""" 
In this solution, we start by making a dict index to store numbers + indicies
We then enumerate through nums
Then we compute the compliment (of current num)
Then we check the current compliment in dict, if does return list of indicies of [complement,i]
Store the current num and index to dict. 
"""