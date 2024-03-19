'''Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false'''

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        list = s.split()
        if(len(list) != len(pattern)):
            return False
        patternToList = {}
        listToPattern = {}
        i = 0
        while i < len(pattern):
            letter = pattern[i]
            word = list[i]
            if letter in patternToList :
                if word != patternToList[letter]:
                    return False
            elif word in listToPattern:
                if letter != listToPattern[word]:
                    return False
            else:
                patternToList[letter] = word
                listToPattern[word] = letter
            i += 1
        return True

if __name__ == "__main__":
    s =  Solution()
    result = s.wordPattern(pattern = "abba", s = "dog dog dog dog")
    print(result)   