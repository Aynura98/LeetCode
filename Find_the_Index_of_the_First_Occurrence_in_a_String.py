'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_len = len(needle)
        haystack_len = len(haystack) - needle_len
        if len(needle) == len(haystack):
            if(needle == haystack):
                return 0
            else: 
                return -1
        else:
            for i in range(haystack_len + 1):
                if haystack[i:needle_len] == needle:
                    return i
                else:
                    i += 1
                    needle_len += 1
        return -1
        

if __name__ == "__main__":
    s =  Solution()
    result = s.strStr("abc", "c")
    print(result)            