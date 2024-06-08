# Group Anagrams LeetCode Solution
# https://leetcode.com/problems/group-anagrams/
# twubz 2024-06-07
"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original 
letters exactly once.

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:            
            count = [0] * 26 # a-z 

            for c in s:
                count[ord(c) - ord("a")] += 1 # subtracting ASCII values to map values to 26.
                
            res[tuple(count)].append(s)

        return res.values()

""" 
We are going to use a Hashmap to group the anagrams together
As a brute force solution of sorting each string has time 
complexity of O(m * n log n)

A hashmap will have complexity of O(m*n*26)
m= length of list of strings
n= length of individual strings
26 = amount of small letter alphabet values (len of count array)
which reduces to O(m*n)
"""