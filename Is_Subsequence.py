class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        for i in range(len(s)):
            if not t[int(s[i])] >= 0:
                return False
        return True

if __name__ == "__main__":
    s =  Solution()
    result = s.isSubsequence(s = "abc", t = "ahbgdc")
    print(result)   