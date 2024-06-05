# Leetcode Valid Anagram Solution
# https://leetcode.com/problems/valid-anagram/description/
# twubz 2024-06-05
"""
Given two strings s and t, return true
if the two strings are anagrams of each
other, otherwise return false.

An anagram is a string that contains the
exact same characters as another string,
but the order of the characters can be
different.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

"""
A simple solution of checking both strings by
using sorted() and checking if both strings are same
"""
