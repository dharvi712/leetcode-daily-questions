940. Distinct Subsequences II
Solved
Hard
Topics
premium lock icon
Companies
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.
 

Example 1:

Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".



class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        end = [0] * 26
        total = 0
        for ch in s:
            i = ord(ch) - 97
            new = (total + 1) % MOD
            total = (total - end[i] + new) % MOD
            end[i] = new
        return total % MOD
