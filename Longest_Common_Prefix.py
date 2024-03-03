'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_length = min(len(s) for s in strs)
        result = ''
        for i in range(min_length):
            current_char = strs[0][i]
            for string in strs:
                if string[i] != current_char:
                    return result
                
            result = result + current_char


        return result
if __name__ == "__main__":
    s =  Solution()
    LCP = s.longestCommonPrefix(["flower","flow","flight"])
    print(LCP)