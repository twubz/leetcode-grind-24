# Duplicate Integer NeetCode Solution
# https://leetcode.com/problems/find-the-duplicate-number/description/
# twubz 2024-06-05
"""
Given an integer array nums, return true if
any value appears more than once in the
array, otherwise return false.
"""
class Solution:
    
    def hasDuplicate(self, nums: list[int]) -> bool:
        
        seen_set = set()
        
        for num in nums:
            
            if num in seen_set:
                
                return True
            
            seen_set.add(num)
            
        return False 

"""
In this solution, I created an empty set,
then iterated through all the nums in the array,
checking if the num is already in the empty set,
then adding that number to the empty set.
"""
