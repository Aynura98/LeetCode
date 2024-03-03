'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                list.append(s[i])
            elif s[i] == ')': 
                if len(list) > 0 and list.pop() == '(':
                    pass
                else:
                    return False
            elif s[i] == '}': 
                if len(list) > 0 and list.pop() == '{':
                    pass
                else:
                    return False
            elif s[i] == ']': 
                if len(list) > 0 and list.pop() == '[':
                    pass
                else:
                    return False
                
            
        return len(list) == 0 
if __name__ == "__main__":
    s =  Solution()
    Valid_parentheses = s.isValid("]")
    print(Valid_parentheses)