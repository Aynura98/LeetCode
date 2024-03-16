class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        list1 = []
        list2 = []
        for i in range(len(s)):
            list1.append(s[i])
        for i in range(len(t)):
            list2.append(t[i])

        return list2 - list1
if __name__ == "__main__":
    s =  Solution()
    result = s.findTheDifference(s = "a", t = "aa")
    print(result)   