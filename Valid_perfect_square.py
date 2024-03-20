class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = 0
        while (x*x != num) :
            if x*x > num:
                return False
            x += 1
        return True



if __name__ == "__main__":
    s =  Solution()
    result = s.isPerfectSquare(num = 14)
    print(result)   