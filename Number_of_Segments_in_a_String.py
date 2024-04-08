class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        list = s.split()
        return len(list)



if __name__ == "__main__":
    s =  Solution()
    result = s.countSegments(s = "Hello, my name is John")
    print(result)   