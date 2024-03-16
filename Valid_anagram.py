class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list = []
        for i in range(len(t)):
            list.append(t[i])
        for i in range(len(s)):
            if s[i] not in list or len(t) != len(s):
                return False
            else:
                list.remove(s[i])
        return True
        
if __name__ == "__main__":
    s =  Solution()
    result = s.isAnagram(s = "aacc", t = "ccac")
    print(result) 