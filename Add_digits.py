'''Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        
        while (len(str_num) != 1):
            sum = 0
            for i in range(len(str_num)):
                sum = sum + int(str_num[i])
            str_num = str(sum)
        return int(str_num)
if __name__ == "__main__":
    s =  Solution()
    result = s.addDigits(num = 38)
    print(result) 