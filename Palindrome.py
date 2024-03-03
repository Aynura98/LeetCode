'''
Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        a = 0
        b = len(string) - 1
        while(a < b):
            if(string[a] == string[b]):
                a+=1
                b-=1
            else:
                return False

        return True
    
if __name__ == "__main__":
    s =  Solution()
    result = s.isPalindrome(121)
    print(result)