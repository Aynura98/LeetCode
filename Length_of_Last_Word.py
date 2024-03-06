'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        Flag = False
        k = 0
        i = len(s) - 1 
        if i == 0:
            return 1
        elif ' ' not in s:
            return len(s)
        while (i >= 0):
            if s[i] == ' ':
                k += 1                
                Flag = s[i - 1] != ' '
                i -= 1
            else:
                Flag = True
            while (Flag ):
                if s[i - 1] == ' ':                 
                    return len(s) - i - k
                
                i -= 1
if __name__ == "__main__":
    s =  Solution()
    result = s.lengthOfLastWord("day   ")
    print(result)   