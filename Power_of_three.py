class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 0
        while (pow(3,x) != n and x >= 0):
            if pow(3,x) > n:
                return False
            x += 1 
        return True
if __name__ == "__main__":
    s =  Solution()
    result = s.isPowerOfThree(n = 25)
    print(result) 