'''
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        i = 0
        length = len(s) - 1
        while (i < length):
            if not s[i].isalnum():
                i += 1
            elif not s[length].isalnum():
                length -= 1
            elif s[i].lower() == s[length].lower():
                i += 1
                length -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    s =  Solution()
    result = s.isPalindrome("A man, a plan, a canal: Panama")
    print(result)   
    aynura = MyNode(1)
    ramazan = MyNode(1)
    child = MyNode(2)
    aynura.next = ramazan
    ramazan.next = child
    



