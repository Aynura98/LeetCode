class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        list = []
        for i in range(len(s)):
            if s[i] not in list:
                list.append(s[i])
        odd = False
        for i in range(len(s)):
            
if __name__ == "__main__":
    s =  Solution()
    result = s.longestPalindrome(s = "abccccdd")
    print(result)   