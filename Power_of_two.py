class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 0
        while (pow(2,x) != n and x >= 0):
            if pow(2,x) > n:
                return False
            x += 1 
        return True


if __name__ == "__main__":
    s =  Solution()
    result = s.isPowerOfTwo(n = 3)
    print(result)   