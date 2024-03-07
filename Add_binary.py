'''
Given two binary strings a and b, return their sum as a binary string. 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_len = max(len(a), len(b)) - 1
        i = 0
        x = 1
        while 

if __name__ == "__main__":
    s =  Solution()
    result = s.addBinary("11","1")
    print(result)   