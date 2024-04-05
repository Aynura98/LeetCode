class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        x = 0
        carry = 0
        answer = []

        while l1 >= 0 or l2 >= 0 or carry > 0:
            digit1 = int(num1[l1]) if l1 >= 0 else 0
            digit2 = int(num2[l2]) if l2 >= 0 else 0

            x = digit1 + digit2 + carry

            carry = x // 10
            x %= 10

            answer.insert(0, str(x))

            if l1 >= 0:
                l1 -= 1
            if l2 >= 0:
                l2 -= 1

        return ''.join(answer)
if __name__ == "__main__":
    s =  Solution()
    result = s.addStrings(num1 = "11", num2 = "123")
    print(result)   