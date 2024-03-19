'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) == 0):
            return False
        
        if len(s) > len(t):
            return False
        
        if len(s) == len(t):
            return s == t

        a_i = 0
        b_i = 0
        while b_i < len(t) and a_i < len(s):
            if s[a_i] == t[b_i]:
                a_i += 1
                
            b_i += 1
            

        return a_i == len(s)
        


if __name__ == "__main__":
    s =  Solution()
    result = s.isSubsequence(s = "b", t = "abc")
    print(result)   