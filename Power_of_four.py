class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 0
        while (pow(4,x) != n and x >= 0):
            if pow(4,x) > n:
                return False
            x += 1
        return True

if __name__ == "__main__":
    s =  Solution()
    result = s.isPowerOfFour(n = 16)
    print(result) 