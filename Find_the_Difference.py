class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
       
        list = []
       
        for i in range(len(t)):
            list.append(t[i])
        for i in range(len(s)):
            if s[i] in list:
                list.remove(s[i])
        return list[0]


if __name__ == "__main__":
    s =  Solution()
    result = s.findTheDifference(s = "", t = "y")
    print(result)   