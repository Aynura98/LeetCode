class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        for char in s:
            if dic[char] == 1:
                return s.index(char)
        return -1
if __name__ == "__main__":
    s =  Solution()
    result = s.firstUniqChar(s = "leetcode")
    print(result)   