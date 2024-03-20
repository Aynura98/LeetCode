class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while (i < j):
            a = s[i]
            b = s[j]
            s[i] = b
            s[j] = a
            i += 1
            j -= 1
        return s
if __name__ == "__main__":
    s =  Solution()
    result = s.reverseString(s = ["h","e","l","l","o"])
    print(result) 