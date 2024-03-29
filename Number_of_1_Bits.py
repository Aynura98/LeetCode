class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n != 0:
            if n & 1 == 1:
                result += 1
            n = n >> 1
        return result
    
if __name__ == "__main__":
    s =  Solution()
    abc = s.hammingWeight(11111111111111111111111111111101)
    print(abc)  
