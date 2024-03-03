'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 0
        length = len(s)
        while (i < len(s)):
            if s[i] == 'I':
                next_index = i + 1

                if next_index < length and s[next_index] == 'V':
                    result = result + 4
                    i += 2
                elif next_index < length and s[next_index] == 'X':
                    result = result + 9
                    i += 2
                else:
                    result = result + 1
                    i += 1
            elif s[i] == 'V':
                result = result + 5
                i += 1
            elif s[i] == 'X':
                next_index = i + 1
                if next_index < length and s[next_index] == 'L':
                    result = result + 40
                    i += 2
                elif next_index < length and s[next_index] == 'C':
                    result = result + 90
                    i += 2
                else:
                    result = result + 10
                    i += 1
            elif s[i] == 'L':
                result = result + 50
                i += 1
            elif s[i] == 'C':
                next_index = i + 1
                if next_index < length and s[next_index] == 'D':
                    result = result + 400
                    i += 2
                elif next_index < length and s[next_index] == 'M':
                    result = result + 900
                    i += 2
                else:
                    result = result + 100
                    i += 1
            elif s[i] == 'D':
                result = result + 500
                i += 1
            elif s[i] == 'M':
                result = result + 1000
                i += 1
        return result
    
if __name__ == "__main__":
    s =  Solution()
    result = s.romanToInt('MCMXCIV')
    print(result)